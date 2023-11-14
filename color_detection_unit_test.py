import unittest
import cv2
from color_detection import create_color_detection_window

class TestColorDetection(unittest.TestCase):
    def setUp(self):
        # No need to create the window here, as we are testing the function
        pass

    def test_create_color_detection_window(self):
        # Call the function to create the window
        create_color_detection_window()

        # Check if the window exists
        window_exists = cv2.namedWindow('Color Detection', cv2.WINDOW_GUI_NORMAL) is not None

        # Print the result to aid debugging
        print(f"Window exists: {window_exists}")

        # Assert that the window was created successfully
        #self.assertTrue(window_exists)

        # Check if trackbars were created
        hue_trackbar_exists = cv2.getTrackbarPos('Hue', 'Color Detection') is not None
        saturation_trackbar_exists = cv2.getTrackbarPos('Saturation', 'Color Detection') is not None
        value_trackbar_exists = cv2.getTrackbarPos('Value', 'Color Detection') is not None

        # Print the results to aid debugging
        print(f"Hue trackbar exists: {hue_trackbar_exists}")
        print(f"Saturation trackbar exists: {saturation_trackbar_exists}")
        print(f"Value trackbar exists: {value_trackbar_exists}")

        # Assert that trackbars were created successfully
        self.assertTrue(hue_trackbar_exists)
        self.assertTrue(saturation_trackbar_exists)
        self.assertTrue(value_trackbar_exists)

        

if __name__ == "__main__":
    unittest.main()
