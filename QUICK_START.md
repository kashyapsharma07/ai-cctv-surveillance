# 🚀 Quick Start Guide - Local Training

## Prerequisites
- Python 3.8 or higher
- Windows PowerShell or Command Prompt
- Webcam (for testing)

## Step 1: Setup Environment
```powershell
# Run the setup script
python setup_training.py
```

This will:
- ✅ Check Python version
- ✅ Install required packages
- ✅ Create necessary directories
- ✅ Verify dataset structure

## Step 2: Train the Model
```powershell
# Start training
python train_model.py
```

**Training Options:**
- **Epochs**: 100 (default) - Number of training cycles
- **Batch Size**: 16 (default) - Images per batch
- **Image Size**: 640 (default) - Input image resolution

**Training Time:**
- CPU: ~2-4 hours
- GPU: ~30-60 minutes

## Step 3: Test the Model
```powershell
# Test with webcam
python realtime_webcam_detection.py
```

**Controls:**
- Press `q` or `Esc` to quit

## Step 4: Launch Web App
```powershell
# Launch the web interface
python launch_app.py
```

## 📁 File Structure
```
AI_CCTV_Surveillance_Updated/
├── train_model.py              # Main training script
├── setup_training.py           # Environment setup
├── realtime_webcam_detection.py # Webcam testing
├── datasets/
│   └── dataset/
│       └── Construction_site_safety_dataset/
│           ├── ppe_data_fixed.yaml  # Fixed dataset config
│           └── css-data/            # Training data
├── app/
│   └── models/
│       └── best.pt             # Trained model (after training)
└── runs/
    └── detect/
        └── ppe_detection_model/ # Training results
```

## 🔧 Troubleshooting

### Common Issues:

1. **"Model not found" error**
   - Run training first: `python train_model.py`

2. **"Dataset not found" error**
   - Ensure dataset is in: `datasets/dataset/Construction_site_safety_dataset/`

3. **"Package not found" error**
   - Run setup: `python setup_training.py`

4. **Webcam not working**
   - Check camera permissions
   - Try different camera index (0, 1, 2)

### Performance Tips:

1. **Use GPU if available**
   - Install CUDA for faster training
   - Model automatically detects GPU

2. **Reduce batch size if out of memory**
   - Change batch_size to 8 or 4

3. **Reduce epochs for quick testing**
   - Use 10-20 epochs for initial testing

## 📊 Training Results

After training, check:
- `runs/detect/ppe_detection_model/weights/best.pt` - Best model
- `runs/detect/ppe_detection_model/results.csv` - Training metrics
- `runs/detect/ppe_detection_model/confusion_matrix.png` - Performance visualization

## 🎯 Model Classes

The model detects 10 classes:
1. Hardhat ✅
2. Mask ✅
3. NO-Hardhat ❌
4. NO-Mask ❌
5. NO-Safety Vest ❌
6. Person 👤
7. Safety Cone 🚧
8. Safety Vest 🦺
9. Machinery 🏗️
10. Vehicle 🚗

## 📞 Support

If you encounter issues:
1. Check the error messages
2. Verify file paths
3. Ensure all requirements are installed
4. Check dataset structure

Happy Training! 🎉 