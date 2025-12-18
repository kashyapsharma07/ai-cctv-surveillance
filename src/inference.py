import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
import streamlit as st
import time
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av
from av.video.frame import VideoFrame
import os

# Class names for the PPE dataset
CLASS_NAMES = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 
               'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

def load_model(model_path):
    """
    Load the YOLOv8 model from given path.
    """
    try:
        model = YOLO(model_path)
        st.success(f"✅ Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

def predict_image(model, image):
    """
    Predict and return image with bounding boxes for uploaded image.
    """
    try:
        img_array = np.array(image.convert("RGB"))
        # Lower confidence threshold to 0.3
        results = model(img_array, conf=0.3)

        # Draw bounding boxes and labels manually
        if results and len(results) > 0 and hasattr(results[0], 'boxes') and results[0].boxes is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            confs = results[0].boxes.conf.cpu().numpy()
            clss = results[0].boxes.cls.cpu().numpy().astype(int)
            for box, conf, cls in zip(boxes, confs, clss):
                x1, y1, x2, y2 = map(int, box)
                label = model.names[cls] if hasattr(model, 'names') and cls < len(model.names) else str(cls)
                color = (0, 255, 0) if 'NO-' not in label else (0, 0, 255)
                cv2.rectangle(img_array, (x1, y1), (x2, y2), color, 2)
                cv2.putText(img_array, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            return img_array
        else:
            st.warning("⚠️ No detections found in the image.")
            return img_array
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
        return np.array(image.convert("RGB"))

class YOLOVideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.model = None
        self.frame_count = 0
        self.last_results = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        self.frame_count += 1
        # Resize for even faster inference
        img_resized = cv2.resize(img, (224, 224))
        # Only run detection every 5th frame
        if self.frame_count % 5 == 0 or self.last_results is None:
            if self.model is not None:
                self.last_results = self.model(img_resized, conf=0.3)
        # Draw boxes on the original frame size for display
        if self.last_results and len(self.last_results) > 0 and hasattr(self.last_results[0], 'boxes') and self.last_results[0].boxes is not None:
            boxes = self.last_results[0].boxes.xyxy.cpu().numpy()
            confs = self.last_results[0].boxes.conf.cpu().numpy()
            clss = self.last_results[0].boxes.cls.cpu().numpy().astype(int)
            # Scale boxes back to original image size
            x_scale = img.shape[1] / 224
            y_scale = img.shape[0] / 224
            for box, conf, cls in zip(boxes, confs, clss):
                x1, y1, x2, y2 = box
                x1 = int(x1 * x_scale)
                y1 = int(y1 * y_scale)
                x2 = int(x2 * x_scale)
                y2 = int(y2 * y_scale)
                label = self.model.names[cls] if hasattr(self.model, 'names') and cls < len(self.model.names) else str(cls)
                color = (0, 255, 0) if 'NO-' not in label else (0, 0, 255)
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cv2.putText(img, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        return VideoFrame.from_ndarray(img, format="bgr24")

def get_or_create_transformer(model):
    # Always create or update the transformer in session state
    if "yolo_transformer" not in st.session_state or st.session_state["yolo_transformer"] is None:
        st.session_state["yolo_transformer"] = YOLOVideoTransformer()
    st.session_state["yolo_transformer"].model = model
    return st.session_state["yolo_transformer"]

def predict_webcam(model):
    st.title("Real-time Webcam Detection")

    webrtc_streamer(
        key="yolo-webcam",
        video_transformer_factory=lambda: get_or_create_transformer(model),
        media_stream_constraints={"video": True, "audio": False},
        async_transform=True,
        rtc_configuration={
            "iceServers": [
                {"urls": [
                    "stun:stun.l.google.com:19302",
                    "stun:stun1.l.google.com:19302",
                    "stun:stun2.l.google.com:19302",
                    "stun:stun3.l.google.com:19302",
                    "stun:stun4.l.google.com:19302"
                ]}
            ] + ([{
                "urls": os.environ.get("TURN_URL"),
                "username": os.environ.get("TURN_USERNAME"),
                "credential": os.environ.get("TURN_CREDENTIAL")
            }] if os.environ.get("TURN_URL") else [])
        },
    )

def get_detection_summary(results):
    """
    Get a summary of detections for display.
    """
    if not results or len(results) == 0:
        return "No detections found"
    
    result = results[0]
    if result.boxes is None or len(result.boxes) == 0:
        return "No detections found"
    
    detections = {}
    for i, box in enumerate(result.boxes.xyxy):
        if hasattr(result.boxes, 'cls') and len(result.boxes.cls) > i:
            cls_id = int(result.boxes.cls[i])
            class_name = CLASS_NAMES[cls_id] if cls_id < len(CLASS_NAMES) else f"Class_{cls_id}"
            detections[class_name] = detections.get(class_name, 0) + 1
    
    summary = []
    for class_name, count in detections.items():
        summary.append(f"{class_name}: {count}")
    
    return ", ".join(summary) if summary else "No detections found"
