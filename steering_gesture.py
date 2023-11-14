import cv2
import imutils
import threading
from imutils.video import VideoStream
from keyboard_input_simulator import PressKey, ReleaseKey, A, D, Space

stop_event = threading.Event()


def image_processing_thread():
    cam = VideoStream(src=0).start()
    cv2.namedWindow("Camera Feed")

    while not stop_event.is_set():
        img = cam.read()
        img = cv2.resize(img, (640, 480))
        img = cv2.flip(img, 1)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        value = (11, 11)
        blurred = cv2.GaussianBlur(hsv, value, 0)
        colourLower = np.array([53, 55, 209])
        colourUpper = np.array([180, 255, 255])

        mask = cv2.inRange(blurred, colourLower, colourUpper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

        height, width = img.shape[:2]

        up_contour = mask[0:height//2, 0:width]
        down_contour = mask[3*height//4:height, 2*width//5:3*width//5]

        key_pressed = False

        if len(cv2.findContours(up_contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]) > 0:
            key_pressed, current_key = process_contours(
                cv2.findContours(up_contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1],
                current_key, A, A, 'LEFT'
            )

        if len(cv2.findContours(down_contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]) > 0:
            key_pressed, current_key = process_contours(
                cv2.findContours(down_contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1],
                current_key, Space, Space, 'NITRO'
            )

            

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

