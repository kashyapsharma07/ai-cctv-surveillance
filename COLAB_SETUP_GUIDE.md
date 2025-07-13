# 🚀 Google Colab GPU Training Guide

## Quick Start Steps

### 1. **Open Google Colab**
- Go to [colab.research.google.com](https://colab.research.google.com)
- Sign in with your Google account

### 2. **Upload the Notebook**
- Click **File > Upload notebook**
- Upload `AI_CCTV_Training_Colab.ipynb` from your computer

### 3. **Enable GPU**
- Click **Runtime > Change runtime type**
- Set **Hardware accelerator** to **GPU**
- Click **Save**

### 4. **Upload Your Dataset**
You have two options:

#### Option A: Upload ZIP File
1. Run the "Upload Dataset" cell in the notebook
2. Click "Choose Files" and select your dataset ZIP
3. Wait for upload and extraction

#### Option B: Use Roboflow (Recommended)
1. Get a free API key from [roboflow.com](https://roboflow.com)
2. Replace `"YOUR_API_KEY"` in the notebook with your actual key
3. Run the download cell

### 5. **Start Training**
- Run all cells in order (Shift + Enter)
- Training will start automatically with GPU acceleration
- Monitor progress in real-time

## 📊 Expected Results

### **Training Time:**
- ⚡ **GPU (T4)**: 30-60 minutes for 100 epochs
- 🐌 **CPU**: 2-4 hours for 100 epochs

### **Performance:**
- 🎯 **mAP50**: 0.8+ (good), 0.9+ (excellent)
- ⚡ **Inference Speed**: 20-50ms per frame
- 📱 **Model Size**: ~6MB (YOLOv8n)

## 🔧 Troubleshooting

### **Common Issues:**

1. **"No GPU available"**
   - Make sure you selected GPU in Runtime settings
   - Try refreshing the page

2. **"Dataset not found"**
   - Check your dataset ZIP file structure
   - Ensure images are in `css-data/train/images/` format

3. **"Out of memory"**
   - Reduce batch size from 16 to 8
   - Use YOLOv8n instead of larger models

4. **"Training too slow"**
   - Verify GPU is enabled
   - Check Colab is not in "busy" state

### **Performance Tips:**

1. **Use T4 GPU** (free tier)
2. **Batch size 16** works well on T4
3. **100 epochs** is usually sufficient
4. **Monitor mAP50** for convergence

## 📥 Download Results

After training completes:

1. **Download Best Model**: `best.pt`
2. **Download Last Model**: `last.pt`
3. **Download Results**: `training_results.zip`

## 🎯 Next Steps

1. **Test locally** with your downloaded model
2. **Integrate** into your CCTV system
3. **Monitor** real-world performance
4. **Retrain** with more data if needed

## 💡 Pro Tips

- **Save your notebook** to Google Drive
- **Use Colab Pro** for longer sessions (12+ hours)
- **Backup models** to Google Drive
- **Share notebooks** with team members

---

**🎉 Ready to train? Open the notebook and start your GPU-powered training!** 