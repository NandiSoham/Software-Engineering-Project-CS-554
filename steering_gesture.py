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
        colourLower = np.array([49, 102, 63])
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
            key_pressed, current_key = process_contours(
                contours_up,
                current_key, KEY_A, KEY_A, 'LEFT', width
            )

        contours_down, _ = cv2.findContours(down_contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours_down) > 0:
            key_pressed, current_key = process_contours(
                contours_down,
                current_key, KEY_D, KEY_D, 'RIGHT', width
            )

        img = cv2.rectangle(img, (0, 0), (width//2 - 35, height//2), (0, 255, 0), 1)
        cv2.putText(img, 'LEFT', (110, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0))

        img = cv2.rectangle(img, (width//2 + 35, 0), (width-2, height//2), (0, 255, 0), 1)
        cv2.putText(img, 'RIGHT', (440, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (139, 0, 0))


        cv2.imshow("Camera Feed", img)
        cv2.waitKey(1)

        if not key_pressed and len(current_key) != 0:
            for current in current_key:
                release_key(current)
            current_key = []

    cam.stop()
    cv2.destroyAllWindows()

def process_contours(contours, key_list, key_press, key_code, key_text, width):
    key = False

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cX = int(M["m10"] / (M["m00"] + 0.000001))

        if cX < (width//2 - 35):
            press_key(key_code)
            key = True
            key_list.append(key_code)
        elif cX > (width // 2 + 35):
            press_key(KEY_D)
            key = True
            key_list.append(KEY_D)

    return key, key_list


if __name__ == "__main__":
    camera_thread = threading.Thread(target=image_processing_thread)
    camera_thread.start()

    try:
        camera_thread.join()
    except KeyboardInterrupt:
        stop_event.set()

