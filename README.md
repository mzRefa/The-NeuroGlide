# 🛸 NeuroGlide AI: Zero-Latency Neural Gesture Interface

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![MediaPipe](https://img.shields.io/badge/engine-MediaPipe-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

**NeuroGlide** is a high-performance Human Interface Device (HID) emulator that transforms standard webcam feeds into a precision, zero-lag virtual mouse. By leveraging MediaPipe's neural hand tracking and custom signal smoothing algorithms, it provides a seamless touchless computing experience.

---

## 🚀 Key Engineering Features

* **Neural Landmark Tracking:** Utilizes MediaPipe’s BlazePalm model for sub-millisecond detection of 21 hand-keypoints.
* **Adaptive Signal Smoothing:** Implements a weighted moving average logic to eliminate hardware "jitter," ensuring a fluid cursor "glide."
* **Zero-Latency Pipeline:** Optimized with `pyautogui.PAUSE = 0` and low-complexity model settings for real-time responsiveness.
* **Intelligent Click Mapping:** Uses Euclidean distance calculation between Thumb (ID 4) and Index (ID 8) tips to trigger hardware click events.

---

## 📂 Repository Architecture

```text
NeuroGlide/
├── 📁 src/
│   ├── tracker.py       # Computer Vision & MediaPipe Logic
│   └── controller.py    # HID Emulation & Smoothing Algorithms
├── 📄 main.py           # Application Entry Point
├── 📄 requirements.txt  # Dependency Manifest
└── 📄 README.md         # Technical Documentation
