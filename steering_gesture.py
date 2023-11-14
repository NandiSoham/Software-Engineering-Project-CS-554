import cv2
import numpy as np
import imutils
import threading
from imutils.video import VideoStream
from keyboard_input_simulator import press_key, release_key, KEY_W, KEY_A, KEY_D, KEY_SPACE

stop_event = threading.Event()
current_key = []

def image_processing_thread():
    global current_key
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

        contours_up, _ = cv2.findContours(up_contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours_up) > 0:
            key_pressed, current_key = contours_up(
                contours_up,
                current_key, KEY_A, KEY_A, 'LEFT'
            )

        contours_down, _ = cv2.findContours(down_contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours_down) > 0:
            key_pressed, current_key = contours_down(
                contours_down,
                current_key, KEY_SPACE, KEY_SPACE, 'NITRO'
            )

        img = cv2.rectangle(img, (0, 0), (width//2 - 35, height//2), (0, 255, 0), 1)
        cv2.putText(img, 'LEFT', (110, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0))

        img = cv2.rectangle(img, (width//2 + 35, 0), (width-2, height//2), (0, 255, 0), 1)
        cv2.putText(img, 'RIGHT', (440, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0))

        img = cv2.rectangle(img, (2*(width//5), 3*(height//4)), (3*width//5, height), (0, 255, 0), 1)
        cv2.putText(img, 'NITRO', (2*(width//5) + 20, height-10), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0))

        cv2.imshow("Camera Feed", img)
        cv2.waitKey(1)

        if not key_pressed and len(current_key) != 0:
            for current in current_key:
                release_key(current)
            current_key = []

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

