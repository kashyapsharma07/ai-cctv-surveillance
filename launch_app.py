#!/usr/bin/env python3
"""
Launch script for the AI CCTV Surveillance System
This script will check if training is complete and launch the web app
"""

import os
import sys
import subprocess
import time

def check_training_status():
    """Check if training has completed"""
    model_path = "runs/detect/train25/weights/best.pt"
    return os.path.exists(model_path)

def check_webapp_model():
    """Check if the web app has the latest model"""
    webapp_model = "app/models/best.pt"
    training_model = "runs/detect/train25/weights/best.pt"
    
    if not os.path.exists(webapp_model):
        return False
    
    if not os.path.exists(training_model):
        return True  # Use existing model
    
    # Compare file modification times
    webapp_time = os.path.getmtime(webapp_model)
    training_time = os.path.getmtime(training_model)
    
    return training_time <= webapp_time

def copy_latest_model():
    """Copy the latest trained model to the web app"""
    source = "runs/detect/train25/weights/best.pt"
    destination = "app/models/best.pt"
    
    if os.path.exists(source):
        try:
            import shutil
            shutil.copy2(source, destination)
            print(f"✅ Updated web app with latest model")
            return True
        except Exception as e:
            print(f"❌ Error copying model: {e}")
            return False
    return False

def launch_streamlit():
    """Launch the Streamlit web application"""
    print("🚀 Launching AI CCTV Surveillance Web App...")
    print("=" * 60)
    print("📱 The app will open in your browser")
    print("🛑 Press Ctrl+C to stop the app")
    print("=" * 60)
    
    try:
        # Launch Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "app/portfolio_app.py", "--server.port", "8501"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Web app stopped by user")
    except Exception as e:
        print(f"❌ Error launching web app: {e}")

def main():
    print("🎯 AI CCTV Surveillance System")
    print("=" * 50)
    
    # Check training status
    if not check_training_status():
        print("⏳ Training not completed yet...")
        print("💡 Please wait for training to finish, then run this script again")
        print("\n📊 To check training progress, look in: runs/detect/train25/")
        return
    
    print("✅ Training completed!")
    
    # Check if web app needs model update
    if not check_webapp_model():
        print("🔄 Updating web app with latest model...")
        if not copy_latest_model():
            print("⚠️ Could not update model, using existing one")
    
    # Launch the web app
    launch_streamlit()

if __name__ == "__main__":
    main() 