import cv2
import numpy as np
from src.tracker import HandTracker
from src.controller import MouseController

def start_neuroglide():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    mouse = MouseController(smoothening=7)

    while cap.isOpened():
        success, frame = cap.read()
        if not success: break
        frame = cv2.flip(frame, 1)

        lms = tracker.find_hand_landmarks(frame)

        if len(lms) != 0:
            # Coordinates
            tx, ty = lms[4][1], lms[4][2]   # Thumb Tip
            ix, iy = lms[8][1], lms[8][2]   # Index Tip
            mx, my = lms[12][1], lms[12][2] # Middle Tip

            # Calculate Euclidean Distances
            left_dist = np.hypot(ix - tx, iy - ty)
            right_dist = np.hypot(mx - tx, my - ty)

            # Gesture Logic
            if left_dist < 35:
                mouse.click(button='left')
                cv2.circle(frame, (ix, iy), 15, (0, 255, 0), cv2.FILLED) # Green for Left
            elif right_dist < 35:
                mouse.click(button='right')
                cv2.circle(frame, (mx, my), 15, (0, 0, 255), cv2.FILLED) # Red for Right
            else:
                # If no fingers are touching, glide the cursor
                mouse.move_mouse(ix, iy)

        cv2.imshow("NeuroGlide Interface", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_neuroglide()
