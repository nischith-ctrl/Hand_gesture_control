# ✋ AI Hand Gesture Control
![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
An AI-based Hand Gesture Control system built using Python, OpenCV, MediaPipe, and PyAutoGUI. This project allows users to control the computer mouse using hand gestures captured through a webcam.

## Hardware Requirements 🖥️
- Laptop/Desktop
- Webcam (Built-in or External)
- Internet connection (for installing required libraries)

## Webcam Configuration 📷
The project uses the default webcam of the laptop.

Make sure the video capture value is set to:

```python
cap = cv2.VideoCapture(0)



## 🚀 Features

- Move mouse cursor by showing only the index finger
- Perform left click by bringing index finger and thumb finger together
- Scroll up using index finger and middle finger gesture
- Scroll down by closing all fingers after index and middle finger gesture
- Real-time hand tracking using webcam
- AI-based gesture recognition using MediaPipe
- Control PC functions using hand gestures

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

## ▶️ How to Run

1. Clone this repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

## 👨‍💻 Author

**Nischith Shettigar**

Engineering Student (Artificial Intelligence & Machine Learning)
