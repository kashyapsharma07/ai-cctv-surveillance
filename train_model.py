#!/usr/bin/env python3
"""
AI CCTV Surveillance - YOLOv8 Training Script
Local Training Script for PPE Detection Model
"""

import os
import sys
import yaml
import shutil
from pathlib import Path
from ultralytics import YOLO
import torch

def check_requirements():
    """Check if all required packages are installed"""
    try:
        import ultralytics
        import torch
        import cv2
        import numpy
        import matplotlib
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def verify_dataset_structure():
    """Verify that the dataset structure is correct"""
    dataset_path = Path("datasets/dataset/Construction_site_safety_dataset")
    yaml_path = dataset_path / "ppe_data_fixed.yaml"
    
    if not dataset_path.exists():
        print(f"❌ Dataset path not found: {dataset_path}")
        return False
    
    if not yaml_path.exists():
        print(f"❌ YAML file not found: {yaml_path}")
        return False
    
    # Check if train/val/test directories exist
    css_data_path = dataset_path / "css-data"
    required_dirs = ["train/images", "valid/images", "test/images"]
    
    for dir_name in required_dirs:
        dir_path = css_data_path / dir_name
        if not dir_path.exists():
            print(f"❌ Required directory not found: {dir_path}")
            return False
        else:
            # Count images in directory
            image_files = list(dir_path.glob("*.jpg")) + list(dir_path.glob("*.jpeg")) + list(dir_path.glob("*.png"))
            print(f"✅ {dir_name}: {len(image_files)} images found")
    
    return True

def load_yaml_config():
    """Load and validate YAML configuration"""
    yaml_path = "datasets/dataset/Construction_site_safety_dataset/ppe_data_fixed.yaml"
    
    try:
        with open(yaml_path, 'r') as file:
            config = yaml.safe_load(file)
        
        print("📋 Dataset Configuration:")
        print(f"   Classes: {config['nc']}")
        print(f"   Class Names: {config['names']}")
        print(f"   Train Path: {config['train']}")
        print(f"   Val Path: {config['val']}")
        print(f"   Test Path: {config['test']}")
        
        return config
    except Exception as e:
        print(f"❌ Error loading YAML config: {e}")
        return None

def train_model(config, epochs=100, batch_size=16, imgsz=640):
    """Train the YOLOv8 model"""
    print(f"\n🚀 Starting YOLOv8 training...")
    print(f"   Epochs: {epochs}")
    print(f"   Batch Size: {batch_size}")
    print(f"   Image Size: {imgsz}")
    
    # Load a YOLOv8 model
    model = YOLO('yolov8n.pt')  # Load pretrained model
    
    # Train the model
    try:
        results = model.train(
            data="datasets/dataset/Construction_site_safety_dataset/ppe_data_fixed.yaml",
            epochs=epochs,
            batch=batch_size,
            imgsz=imgsz,
            device='cpu',  # Use GPU if available, else CPU
            project='runs/detect',
            name='ppe_detection_model',
            patience=20,  # Early stopping patience
            save=True,
            save_period=10,  # Save every 10 epochs
            verbose=True
        )
        
        print("✅ Training completed successfully!")
        return results
        
    except Exception as e:
        print(f"❌ Training failed: {e}")
        return None

def validate_model():
    """Validate the trained model"""
    print("\n🔍 Validating model...")
    
    # Find the best model
    model_path = "runs/detect/ppe_detection_model/weights/best.pt"
    
    if not os.path.exists(model_path):
        print(f"❌ Best model not found at: {model_path}")
        return False
    
    try:
        model = YOLO(model_path)
        
        # Validate on test set
        results = model.val(
            data="datasets/dataset/Construction_site_safety_dataset/ppe_data_fixed.yaml",
            split='test'
        )
        
        print("✅ Model validation completed!")
        return True
        
    except Exception as e:
        print(f"❌ Model validation failed: {e}")
        return False

def main():
    """Main training function"""
    print("=" * 60)
    print("🤖 AI CCTV Surveillance - YOLOv8 Training")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        return
    
    # Verify dataset structure
    if not verify_dataset_structure():
        print("\n❌ Dataset structure verification failed!")
        print("Please ensure your dataset is properly organized.")
        return
    
    # Load configuration
    config = load_yaml_config()
    if not config:
        return
    
    # Training parameters
    epochs = 100
    batch_size = 16
    imgsz = 640
    
    # Check if user wants to customize parameters
    print(f"\n📝 Current training parameters:")
    print(f"   Epochs: {epochs}")
    print(f"   Batch Size: {batch_size}")
    print(f"   Image Size: {imgsz}")
    
    custom = input("\nDo you want to customize these parameters? (y/n): ").lower().strip()
    
    if custom == 'y':
        try:
            epochs = int(input(f"Enter number of epochs (current: {epochs}): ") or epochs)
            batch_size = int(input(f"Enter batch size (current: {batch_size}): ") or batch_size)
            imgsz = int(input(f"Enter image size (current: {imgsz}): ") or imgsz)
        except ValueError:
            print("❌ Invalid input. Using default parameters.")
    
    # Start training
    results = train_model(config, epochs, batch_size, imgsz)
    
    if results:
        # Validate model
        validate_model()
        
        print("\n🎉 Training pipeline completed!")
        print("📁 Check the 'runs/detect/ppe_detection_model' folder for results.")
        print("📊 Best model saved as: runs/detect/ppe_detection_model/weights/best.pt")
        
        # Copy best model to app directory for easy access
        best_model_path = "runs/detect/ppe_detection_model/weights/best.pt"
        app_model_path = "app/models/best.pt"
        
        if os.path.exists(best_model_path):
            os.makedirs("app/models", exist_ok=True)
            shutil.copy2(best_model_path, app_model_path)
            print(f"✅ Best model copied to: {app_model_path}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main() 