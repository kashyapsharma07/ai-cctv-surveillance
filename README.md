# 🛡️ AI CCTV Surveillance System

## Overview
This project implements a comprehensive YOLOv8-based object detection system for construction site safety monitoring. It detects Personal Protective Equipment (PPE) like helmets, masks, safety vests, and identifies safety violations in real-time.

## 🎯 Features

### Detection Classes (10 Classes)
- **🟢 Compliant PPE:** Hardhat, Mask, Safety Vest, Safety Cone
- **🔴 Safety Violations:** NO-Hardhat, NO-Mask, NO-Safety Vest
- **👥 Other Objects:** Person, Machinery, Vehicle

### Application Features
- **📷 Single Image Detection** - Upload and analyze individual images
- **📁 Batch Image Processing** - Process multiple images at once
- **📹 Real-time Webcam Detection** - Live video stream analysis
- **🎨 Beautiful Web Interface** - Modern Streamlit-based UI
- **📊 Detection Summaries** - Detailed analysis reports

## 🏗️ Project Structure
```
AI_CCTV_Surveillance_Updated/
├── app/                           # Web application
│   ├── main.py                   # Streamlit web app
│   ├── models/                   # Trained model weights
│   └── assets/                   # Static assets
├── src/                          # Core functionality
│   ├── train.py                  # Model training script
│   ├── inference.py              # Detection and prediction
│   └── dataset.py                # Dataset handling
├── datasets/                     # Training datasets
│   └── dataset/Construction_site_safety_dataset/
│       ├── css-data/             # Main dataset (2,600+ images)
│       └── ppe_data_fixed.yaml   # Dataset configuration
├── runs/                         # Training outputs
├── notebooks/                    # Jupyter notebooks
├── setup.py                      # Environment setup script
├── test_model.py                 # Model testing script
├── launch_app.py                 # App launcher
└── requirements.txt              # Python dependencies
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Clone or download the project
cd AI_CCTV_Surveillance_Updated

# Run setup script (recommended)
python setup.py

# Or install dependencies manually
pip install -r requirements.txt
```

### 2. Train the Model
```bash
# Start training (10 epochs, ~6-13 hours on CPU)
python src/train.py --data datasets/dataset/Construction_site_safety_dataset/ppe_data_fixed.yaml --model yolov8n.pt --epochs 10

# For faster testing (3-5 epochs)
python src/train.py --data datasets/dataset/Construction_site_safety_dataset/ppe_data_fixed.yaml --model yolov8n.pt --epochs 5
```

### 3. Test the Model
```bash
# Test the trained model
python test_model.py
```

### 4. Launch Web Application
```bash
# Launch the web app
python launch_app.py

# Or run directly with Streamlit
streamlit run app/main.py
```

## 📊 Dataset Information

- **Training Images:** 2,600+ images
- **Validation Images:** 114 images
- **Test Images:** Available for evaluation
- **Classes:** 10 different PPE and safety-related objects
- **Format:** YOLO format with bounding box annotations

## ⚙️ Configuration

### Training Parameters
- **Model:** YOLOv8n (nano version for speed)
- **Image Size:** 640x640 pixels
- **Batch Size:** 16 (adjustable)
- **Epochs:** 10 (recommended), 3-5 for testing
- **Optimizer:** SGD with momentum

### Hardware Requirements
- **Minimum:** CPU with 8GB RAM
- **Recommended:** GPU for faster training
- **Storage:** 5GB free space

## 🎨 Web Application Features

### Single Image Detection
- Upload individual images
- Real-time detection results
- Detailed object analysis
- Confidence scores

### Batch Processing
- Upload multiple images
- Batch analysis
- Summary reports
- Export capabilities

### Real-time Webcam
- Live video stream
- Real-time detection
- Safety violation alerts
- Performance monitoring

## 🔧 Advanced Usage

### Custom Training
```bash
# Train with custom parameters
python src/train.py \
    --data your_dataset.yaml \
    --model yolov8s.pt \
    --epochs 50 \
    --batch 32 \
    --imgsz 640
```

### Model Validation
```bash
# Validate data paths before training
python src/train.py --data your_dataset.yaml --model yolov8n.pt --validate
```

### Performance Optimization
- Use GPU for faster training
- Reduce batch size for limited memory
- Adjust image size for speed/accuracy trade-off
- Use early stopping to prevent overfitting

## 📈 Performance Metrics

### Expected Results
- **Detection Accuracy:** 80-90% (with 10 epochs)
- **Training Time:** 6-13 hours (CPU), 1-3 hours (GPU)
- **Inference Speed:** 30-60 FPS (CPU), 100+ FPS (GPU)

### Model Variants
- **YOLOv8n:** Fastest, good for real-time
- **YOLOv8s:** Balanced speed/accuracy
- **YOLOv8m:** Higher accuracy, slower
- **YOLOv8l:** Best accuracy, slowest

## 🛠️ Troubleshooting

### Common Issues
1. **Model not found:** Ensure `best.pt` is in `app/models/`
2. **Training slow:** Use GPU or reduce epochs/batch size
3. **Webcam not working:** Check camera permissions
4. **Memory errors:** Reduce batch size or image size

### Support
- Check `project_status.md` for current status
- Review training logs in `runs/detect/`
- Test with `test_model.py` for validation

## 📝 License
This project is for educational and research purposes. Please ensure compliance with local regulations when deploying in production environments.

## 🤝 Contributing
Feel free to submit issues, feature requests, or pull requests to improve the project.

---

**Built with ❤️ using YOLOv8 and Streamlit**
