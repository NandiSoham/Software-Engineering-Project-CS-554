import unittest
import numpy as np
import cv2

# Assuming get_color_mask is in the same file, otherwise adjust the import
from color_detection import get_color_mask

class TestColorDetection(unittest.TestCase):

# ... other parts of your test code ...

 def test_get_color_mask(self):
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame[:, :, :] = [100, 150, 200]  # Set a specific BGR color

    # Convert BGR to HSV and get the HSV values of this color
    hsv_color = cv2.cvtColor(np.uint8([[frame[0, 0]]]), cv2.COLOR_BGR2HSV).flatten()

    result = get_color_mask(hsv_color[0], hsv_color[1], hsv_color[2], frame)

    # ... rest of your test code ...

if __name__ == '__main__':
    unittest.main()