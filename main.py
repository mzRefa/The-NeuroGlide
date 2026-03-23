import cv2
import numpy as np
from src.tracker import HandTracker
from src.controller import MouseController

def start_neuroglide():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    mouse = MouseController(smoothening=7) # Increase for more "Glide"

    while cap.isOpened():
        success, frame = cap.read()
        if not success: break
        frame = cv2.flip(frame, 1) # Mirror the image

        # Get landmarks from the tracker
        lms = tracker.find_hand_landmarks(frame)

        if len(lms) != 0:
            # Index finger tip (ID 8) and Thumb tip (ID 4)
            ix, iy = lms[8][1], lms[8][2]
            tx, ty = lms[4][1], lms[4][2]

            # Calculate distance for clicking
            dist = np.hypot(ix - tx, iy - ty)

            if dist > 35:
                # If fingers are apart, just move
                mouse.move_mouse(ix, iy)
            else:
                # If fingers touch, click!
                mouse.click()

        cv2.imshow("NeuroGlide Interface", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_neuroglide()
