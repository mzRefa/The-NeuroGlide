import pyautogui
import numpy as np

class MouseController:
    def __init__(self, smoothening=5):
        self.screen_w, self.screen_h = pyautogui.size()
        self.smoothening = smoothening
        self.plocX, self.plocY = 0, 0 # Previous locations
        # Disable pyautogui delay for "Zero-Latency" feel
        pyautogui.PAUSE = 0

    def move_mouse(self, x, y):
        # 1. Map camera coordinates to screen resolution
        # We use a smaller "active box" (150 to 500) so you don't have to 
        # move your hand across the entire camera view.
        fx = np.interp(x, (150, 490), (0, self.screen_w))
        fy = np.interp(y, (150, 330), (0, self.screen_h))

        # 2. The "Glide" (Smoothening)
        clocX = self.plocX + (fx - self.plocX) / self.smoothening
        clocY = self.plocY + (fy - self.plocY) / self.smoothening

        # 3. Move the actual hardware cursor
        pyautogui.moveTo(clocX, clocY)
        
        # 4. Update previous location for next frame
        self.plocX, self.plocY = clocX, clocY

    def click(self, button='left'):
        pyautogui.click(button=button)
