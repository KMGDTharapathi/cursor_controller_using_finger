import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import numpy as np
import time

# Screen size
wScr, hScr = pyautogui.size()

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Hand detector
detector = HandDetector(maxHands=1, detectionCon=0.7)
smoothening = 7

# Previous cursor position
px, py = 0, 0

# Drag state
dragging = False

# Scroll state
scroll_prev = None

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)

        # Finger tip positions
        xIndex, yIndex = lmList[8][0], lmList[8][1]   # Index
        xMiddle, yMiddle = lmList[12][0], lmList[12][1] # Middle
        xRing, yRing = lmList[16][0], lmList[16][1]   # Ring

        # ---------------- Move mode ----------------
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0:
            x3 = np.interp(xIndex, (0, 640), (0, wScr))
            y3 = np.interp(yIndex, (0, 480), (0, hScr))
            cx = px + (x3 - px) / smoothening
            cy = py + (y3 - py) / smoothening
            pyautogui.moveTo(cx, cy)
            px, py = cx, cy

        # ---------------- Left Click ----------------
        if fingers[1] == 1 and fingers[2] == 1:
            distance, _, _ = detector.findDistance(lmList[8], lmList[12])
            if distance < 35 and not dragging:
                pyautogui.click()
                time.sleep(0.2)

        # ---------------- Drag & Drop ----------------
        if fingers[1] == 1 and fingers[2] == 1:
            distance, _, _ = detector.findDistance(lmList[8], lmList[12])
            if distance < 35:
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

        # ---------------- Right Click ----------------
        if fingers[1] == 1 and fingers[3] == 1:
            distance, _, _ = detector.findDistance(lmList[8], lmList[16])
            if distance < 35:
                pyautogui.rightClick()
                time.sleep(0.2)

        # ---------------- Scroll ----------------
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0:
            if scroll_prev is not None:
                dy = yIndex - scroll_prev
                if abs(dy) > 20:
                    if dy > 0:
                        pyautogui.scroll(-100)  # scroll down
                    else:
                        pyautogui.scroll(100)   # scroll up
            scroll_prev = yIndex
        else:
            scroll_prev = None

    cv2.imshow("Hand Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
