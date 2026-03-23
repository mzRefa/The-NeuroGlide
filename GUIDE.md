# 🎮 NeuroGlide Gesture Guide

To achieve the best performance with **NeuroGlide**, ensure your hand is 0.5m – 1.5m from the webcam in a well-lit environment.

### 🖱️ Command Reference

| Action | Technical Logic | Gesture |
| :--- | :--- | :--- |
| **Precision Move** | Linear Interpolation | Move **Index Tip** (ID 8) |
| **Left Click** | Euclidean Distance < 35px | Pinch **Thumb** (4) + **Index** (8) |
| **Right Click** | Euclidean Distance < 35px | Pinch **Thumb** (4) + **Middle** (12) |
| **System Exit** | Key Listener | Press **'q'** |

### 🧠 How it Works
The system uses the **BlazePalm** model to identify 21 coordinates. 



By calculating the hypotenuse between the Thumb and other fingertips, we can trigger hardware events through the `pyautogui` library without physical contact.
