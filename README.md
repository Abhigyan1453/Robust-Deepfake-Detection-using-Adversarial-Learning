# Robust-Deepfake-Detection-using-Adversarial-Learning
This project focuses on leveraging Adversarial Learning techniques to enhance the robustness of Deepfake Detection systems against evolving manipulation methods.
# Robust Deepfake Detection using Adversarial Learning

This repository contains the implementation of a deep learning-based system designed to detect manipulated media (Deepfakes). The project leverages **Adversarial Learning** techniques to enhance detection robustness against various sophisticated forgery methods.

## 🚀 Overview
As deepfake technology evolves, traditional detection models often struggle with unseen manipulation techniques. This project focuses on:
- Improving detection accuracy using robust feature extraction.
- Utilizing Adversarial Learning to stay ahead of generative forgery.
- Providing a user-friendly web interface for real-time detection.

## 📂 Project Structure
- `app.py`: Flask-based web server for the application.
- `detect.py`: Core inference script for deepfake detection.
- `model.py`: Deep Learning model architecture.
- `utils.py`: Helper functions for image/video preprocessing.
- `templates/ & statics/`: Frontend assets (HTML, CSS, JS).
- `requirements.txt`: List of dependencies required to run the project.

## 🧠 Pre-trained Model Weights
The trained model file (`model.pth`) exceeds GitHub's file size limit. You can download the weights from the link below:

👉 **[Download Model Weights (Google Drive)](https://drive.google.com/drive/folders/1eYpFt0WYKTgY2kMpvcAmaNPJRG2Idnzq?usp=sharing)**

> **Note:** After downloading, place the `model.pth` file in the root directory of the project.

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash```
### 2. Download the model.pth file from the Google Drive link provided above and place it in the project folder.
### 3. Install Dependencies
      Ensure you have Python installed, then run:
```pip install -r requirements.txt```
### 4. Run the Application
```python app.py```

The application will be available at http://127.0.0.1:5000/.
git clone [https://github.com/Abhigyan1453/Robust-Deepfake-Detection-using-Adversarial-Learning.git](https://github.com/Abhigyan1453/Robust-Deepfake-Detection-using-Adversarial-Learning.git)
cd Robust-Deepfake-Detection-using-Adversarial-Learning
