import cv2
import unittest
from unittest.mock import patch, MagicMock
from steering_gesture import image_processing_thread, stop_event

class TestImageProcessingThread(unittest.TestCase):

    @patch('cv2.namedWindow')
    @patch('imutils.video.VideoStream')
    @patch('cv2.imshow')
    @patch('cv2.waitKey', return_value=27)  # Simulate ESC key press to exit
    @patch('cv2.destroyAllWindows')
    def test_image_processing_thread(self, mock_destroyAllWindows, mock_waitKey, mock_imshow, mock_VideoStream, mock_namedWindow):
        mock_cam = MagicMock()
        mock_VideoStream.return_value = mock_cam

        image_processing_thread()

        mock_VideoStream.assert_called_once_with(src=0)
        mock_cam.start.assert_called_once()
        mock_namedWindow.assert_called_once_with("Camera Feed")

        self.assertTrue(stop_event.is_set())  # Ensure stop_event is set after the KeyboardInterrupt

        mock_cam.stop.assert_called_once()
        mock_destroyAllWindows.assert_called_once()

if __name__ == '__main__':
    unittest.main()