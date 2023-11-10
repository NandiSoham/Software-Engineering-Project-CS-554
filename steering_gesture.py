import cv2
import imutils
import threading
from imutils.video import VideoStream


stop_event = threading.Event()


def image_processing_thread():
    cam = VideoStream(src=0).start()
    cv2.namedWindow("Camera Feed")

    while not stop_event.is_set():
        img = cam.read()
        img = cv2.resize(img, (640, 480))
        img = cv2.flip(img, 1)  # Flipping the image horizontally
        cv2.imshow("Camera Feed", img)
        cv2.waitKey(1)

    cam.stop()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    camera_thread = threading.Thread(target=image_processing_thread)
    camera_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        stop_event.set()
