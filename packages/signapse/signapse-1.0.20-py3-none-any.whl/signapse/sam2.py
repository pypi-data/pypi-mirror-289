import os
import cv2
import imageio
import shutil
import torch
import numpy as np
import subprocess
from pathlib import Path
from sam2.build_sam import build_sam2_video_predictor
import mediapipe as mp
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def get_wrist_points(frame):
    height, width, _ = frame.shape
    
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with MediaPipe Pose
    results = pose.process(rgb_frame)
    
    if results.pose_landmarks:
        left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        nose = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
        
        left_wrist_coords = [int(left_wrist.x * width), int(left_wrist.y * height)]
        right_wrist_coords = [int(right_wrist.x * width), int(right_wrist.y * height)]
        face_center_coords = [int(nose.x * width), int(nose.y * height)]
        
        return left_wrist_coords, right_wrist_coords, face_center_coords
    else:
        return None, None, None
    
def save_masks( no_frame_names, video_segments, vis_frame_stride=1):
    mask=[]
    for out_frame_idx in range(0, no_frame_names, vis_frame_stride):        
        for _, out_mask in video_segments[out_frame_idx].items():
            mask.append(out_mask)

    return mask

class SAM2Initializer:
    def __init__(self, checkpoint_path, model_config_path):
        self.checkpoint_path = checkpoint_path
        self.model_config_path = model_config_path

        # Ensure we're using bfloat16 precision for the entire notebook
        self.autocast = torch.autocast(device_type="cuda", dtype=torch.bfloat16)
        self.autocast.__enter__()

        # Check for GPU compatibility
        if torch.cuda.is_available() and torch.cuda.get_device_properties(0).major >= 8:
            torch.backends.cuda.matmul.allow_tf32 = True
            torch.backends.cudnn.allow_tf32 = True

        # Build the SAM 2 predictor
        self.predictor = self._initialize_predictor()

    def _initialize_predictor(self):
        """Initialize the SAM 2 video predictor."""
        return build_sam2_video_predictor(self.model_config_path, self.checkpoint_path)

    def get_predictor(self):
        """Return the initialized predictor."""
        return self.predictor

    def extract_frames(self, video_path, image_dir, ending_frame = None):
        reader = imageio.get_reader(video_path)
        fps = reader.get_meta_data().get('fps', None)
        reader.close()
        if fps is not None:
            if fps == 0:
                raise ValueError("FPS is 0, which is invalid")
        else:
            raise ValueError("FPS not found in video metadata")
    
        Path(image_dir).mkdir(parents=True, exist_ok=True)
        output_pattern = Path(image_dir) / '%05d.jpg'

        ffmpeg_command = [
            'ffmpeg',
            '-i', video_path,
            '-q:v', '2',
            '-start_number', '0',
            '-pix_fmt', 'yuvj420p'
            # str(output_pattern)
        ]
        if ending_frame > 0:
            ffmpeg_command.extend(['-frames:v', str(ending_frame)])
        ffmpeg_command.extend([str(output_pattern)])

        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f"Frames extracted and saved to: {image_dir}")
            return fps
        except subprocess.CalledProcessError as e:
            shutil.rmtree(image_dir)  # Clean up if error occurs
            raise ValueError(f"An error occurred while extracting frames: {e}")
    
    def predict(self,points, labels, ann_frame_idx, ann_obj_id, predictor, inference_state):
        points = np.array(points, dtype=np.float32)
        labels = np.array(labels, np.int32)

        _, out_obj_ids, out_mask_logits = predictor.add_new_points(
            inference_state=inference_state,
            frame_idx=ann_frame_idx,
            obj_id=ann_obj_id,
            points=points,
            labels=labels,
        )

        video_segments = {}
        for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
            video_segments[out_frame_idx] = {
                out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
                for i, out_obj_id in enumerate(out_obj_ids)
            }
        return video_segments


def get_masks_sam2(input_video, stop, tmp_dir = "./inputs/tmp"):
    model_cfg ="sam2_hiera_l.yaml"
    sam2_checkpoint ="/home/basheer/Signapse/Codes/SAM2/segment-anything-2/checkpoints/sam2_hiera_large.pt"

    base_name = os.path.basename(input_video)
    filename, _ = os.path.splitext(base_name)
    tmp_image_dir = os.path.join(tmp_dir, filename)

    sam2_initializer = SAM2Initializer(sam2_checkpoint, model_cfg)
    predictor = sam2_initializer.get_predictor()
    sam2_initializer.extract_frames(input_video, tmp_image_dir , ending_frame = stop)

    frame_names = [p for p in os.listdir(tmp_image_dir) if os.path.splitext(p)[-1] in [".jpg", ".jpeg", ".JPG", ".JPEG"]]
    frame_names.sort(key=lambda p: int(os.path.splitext(p)[0]))

    inference_state = predictor.init_state(video_path=tmp_image_dir)
    predictor.reset_state(inference_state)

    first_frame = cv2.imread(os.path.join(tmp_image_dir,'00000.jpg'))
    left_wrist_coords, right_wrist_coords, face_center_coords = get_wrist_points(first_frame)

    # points, labels = [], []
    # for i in range(0, len(left_wrist_coords), int(len(left_wrist_coords)/4)):
    # i = 0
    # points.append((left_wrist_coords[i].cpu() * torch.tensor([first_frame.shape[1], first_frame.shape[0]])).int().tolist())
    # labels.append(1)
    # points.append((right_wrist_coords[i].cpu() * torch.tensor([first_frame.shape[1], first_frame.shape[0]])).int().tolist())
    # labels.append(1)

    points = [left_wrist_coords,right_wrist_coords,face_center_coords]#[[900, 950], [1200, 950]]
    labels = [1,1,0]  # Exclude the face for now
    ann_frame_idx = 0
    ann_obj_id = 1

    video_segments = sam2_initializer.predict(points,labels, ann_frame_idx, ann_obj_id, predictor, inference_state)
    masks = save_masks(len(frame_names), video_segments)
    shutil.rmtree(tmp_image_dir)
    return masks
