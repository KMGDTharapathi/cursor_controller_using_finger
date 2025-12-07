# Hand Gesture Mouse Control

Control your computer mouse using hand gestures through your webcam — built with OpenCV, CVZone, Mediapipe, PyAutoGUI, and NumPy.

---

## Overview

This project uses computer vision to track hand movements and convert them into mouse actions.
Using only your webcam, you can:

* Move the mouse cursor
* Perform left click
* Perform right click
* Drag and drop
* Scroll up or down

It is powered by:

* OpenCV for video processing
* CVZone/Mediapipe for hand landmark detection
* PyAutoGUI for mouse control
* NumPy for coordinate mapping

---

## Features

* Smooth mouse movement
* Touchless left click
* Touchless right click
* Drag and drop gesture
* Scroll using finger motion
* Lightweight dependency setup
* Works on Windows, macOS, and Linux

---

## Gesture Controls

| Gesture                         | Action            |
| ------------------------------- | ----------------- |
| Index finger up                 | Move mouse cursor |
| Index + Middle fingers touching | Left click / Drag |
| Index + Ring fingers touching   | Right click       |
| Index finger vertical movement  | Scroll            |

---

## Installation

Install the required libraries:

```bash
pip install opencv-python cvzone mediapipe pyautogui numpy
```

If cvzone gives problems:

```bash
pip install cvzone==1.5.6
```

---

## How to Run

1. Clone or download this project
2. Navigate to the project folder
3. Run the script:

```bash
python hand_mouse.py
```

4. Make sure your webcam is enabled
5. Press `Q` to quit the application

---

## How It Works

### Webcam Capture

Reads frames from the webcam:

```python
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
```

### Hand Tracking

Detects hand and 21 key landmarks:

```python
detector = HandDetector(maxHands=1, detectionCon=0.7)
```

### Mouse Movement

Maps finger coordinates to screen size:

```python
pyautogui.moveTo(cx, cy)
```

### Left Click

Triggered when index and middle fingers get close:

```python
pyautogui.click()
```

### Right Click

Triggered when index and ring fingers get close:

```python
pyautogui.rightClick()
```

### Dragging

Holds the mouse when fingers stay together:

```python
pyautogui.mouseDown()
pyautogui.mouseUp()
```

### Scrolling

Scrolls based on vertical finger movement:

```python
pyautogui.scroll(100)
```

---

## Project Structure

```
HandGestureMouse/
│── hand_mouse.py
│── README.md
└── requirements.txt   (optional)
```

---

## Troubleshooting

### Webcam not detected

Try:

```python
cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(2)
```

### Hand not detected

* Improve lighting
* Ensure your whole hand is visible
* Keep your hand in front of the camera

### Mouse movement lag

Reduce the smoothening value:

```python
smoothening = 5
```

---

## Author

**Dakshina Tharapathi**
GitHub: [https://github.com/KMGDTharapathi](https://github.com/KMGDTharapathi)

