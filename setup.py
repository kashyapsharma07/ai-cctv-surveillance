#!/usr/bin/env python3
"""
Setup script for AI CCTV Surveillance System
Handles environment setup, model download, and dataset preparation
"""

import os
import sys
import argparse
import subprocess
import urllib.request
import zipfile
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        "app/models",
        "app/assets",
        "logs",
        "runs/detect"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ Directories created successfully!")

def download_model():
    """Download the trained model"""
    print("🤖 Downloading trained model...")
    
    # Model URLs (you'll need to update these with actual URLs)
    model_urls = {
        "best.pt": "https://drive.google.com/uc?export=download&id=YOUR_MODEL_ID",
        "last.pt": "https://drive.google.com/uc?export=download&id=YOUR_MODEL_ID"
    }
    
    model_dir = Path("app/models")
    model_dir.mkdir(parents=True, exist_ok=True)
    
    for model_name, url in model_urls.items():
        model_path = model_dir / model_name
        if not model_path.exists():
            try:
                print(f"📥 Downloading {model_name}...")
                # Note: You'll need to implement proper Google Drive download
                # For now, we'll create a placeholder
                with open(model_path, 'w') as f:
                    f.write("# Placeholder model file\n")
                    f.write("# Please download the actual model from the provided URL\n")
                print(f"⚠️ Created placeholder for {model_name}")
                print(f"📋 Please download from: {url}")
            except Exception as e:
                print(f"❌ Error downloading {model_name}: {e}")
        else:
            print(f"✅ {model_name} already exists")

def download_dataset():
    """Download the dataset"""
    print("📁 Downloading dataset...")
    
    # Dataset URLs (you'll need to update these with actual URLs)
    dataset_urls = {
        "Construction_site_safety_dataset.zip": "https://drive.google.com/uc?export=download&id=YOUR_DATASET_ID",
        "helmet-100.v1i.yolov8.zip": "https://drive.google.com/uc?export=download&id=YOUR_DATASET_ID"
    }
    
    dataset_dir = Path("datasets/dataset")
    dataset_dir.mkdir(parents=True, exist_ok=True)
    
    for dataset_name, url in dataset_urls.items():
        dataset_path = dataset_dir / dataset_name
        if not dataset_path.exists():
            try:
                print(f"📥 Downloading {dataset_name}...")
                # Note: You'll need to implement proper Google Drive download
                # For now, we'll create a placeholder
                with open(dataset_path, 'w') as f:
                    f.write("# Placeholder dataset file\n")
                    f.write("# Please download the actual dataset from the provided URL\n")
                print(f"⚠️ Created placeholder for {dataset_name}")
                print(f"📋 Please download from: {url}")
            except Exception as e:
                print(f"❌ Error downloading {dataset_name}: {e}")
        else:
            print(f"✅ {dataset_name} already exists")

def check_environment():
    """Check if the environment is properly set up"""
    print("🔍 Checking environment...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    
    print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Check if key packages are available
    required_packages = ['streamlit', 'ultralytics', 'opencv-python', 'torch']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}")
    
    if missing_packages:
        print(f"\n⚠️ Missing packages: {', '.join(missing_packages)}")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Setup AI CCTV Surveillance System")
    parser.add_argument("--install-requirements", action="store_true", help="Install required packages")
    parser.add_argument("--download-model", action="store_true", help="Download trained model")
    parser.add_argument("--download-dataset", action="store_true", help="Download dataset")
    parser.add_argument("--check-env", action="store_true", help="Check environment")
    parser.add_argument("--all", action="store_true", help="Run all setup steps")
    
    args = parser.parse_args()
    
    print("🛡️ AI CCTV Surveillance System Setup")
    print("=" * 50)
    
    if args.all or args.install_requirements:
        install_requirements()
    
    if args.all or not any([args.install_requirements, args.download_model, args.download_dataset, args.check_env]):
        create_directories()
        install_requirements()
    
    if args.all or args.download_model:
        download_model()
    
    if args.all or args.download_dataset:
        download_dataset()
    
    if args.all or args.check_env:
        check_environment()
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Download the trained model from the provided URL")
    print("2. Download the dataset from the provided URL")
    print("3. Run: python launch_app.py")
    print("4. Or run: streamlit run app/portfolio_app.py")

if __name__ == "__main__":
    main() 