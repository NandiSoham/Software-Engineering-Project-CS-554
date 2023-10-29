import cv2
import imutils
from imutils.video import VideoStream

def image_processing_thread():
    cam = VideoStream(src=0).start()
    cv2.namedWindow("Camera Feed")
    cam.stop()
    cv2.destroyAllWindows() 