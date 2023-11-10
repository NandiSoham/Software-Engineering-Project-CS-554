import cv2
import numpy as np


def create_color_detection_window():
    cv2.namedWindow('Color Detection')
    cv2.createTrackbar('Hue', 'Color Detection', 0, 179, on_trackbar_change)
    cv2.createTrackbar('Saturation', 'Color Detection',
                       0, 255, on_trackbar_change)
    cv2.createTrackbar('Value', 'Color Detection', 0, 255, on_trackbar_change)


def on_trackbar_change(x):
    pass


def get_color_mask(hue, saturation, value, frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
<<<<<<< HEAD
    
    lower_color = np.array([hue, saturation, value], dtype=np.uint8)
    upper_color = np.array([180, 255, 255], dtype=np.uint8) 
=======

    lower_color = np.array([hue, saturation, value])
    upper_color = np.array([180, 255, 255])
>>>>>>> 80ae4b6dcdea0a2ed8c68c6a2e51ae6ef7fcc742

    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    return result


def main():
    cap = cv2.VideoCapture(0)
    create_color_detection_window()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        height, width, _ = frame.shape
        height, width, _ = frame.shape

        box_height = int(height / 3)
        top_boxes = frame[:2*box_height, :]
        bottom_box = frame[2*box_height:, :]

        hue = cv2.getTrackbarPos('Hue', 'Color Detection')
        saturation = cv2.getTrackbarPos('Saturation', 'Color Detection')
        value = cv2.getTrackbarPos('Value', 'Color Detection')
        result = get_color_mask(hue, saturation, value, frame)

<<<<<<< HEAD
        cv2.imshow('Color Detection', frame)
    
        frame = cv2.rectangle(frame, (0, 0), (width, 2*box_height), (0, 255, 0), 2)
        frame = cv2.rectangle(frame, (0, 2*box_height), (width, height), (0, 255, 0), 2)

        cv2.imshow('Camera Feed', frame)
=======
        cv2.imshow('Color Detection', result)
>>>>>>> 80ae4b6dcdea0a2ed8c68c6a2e51ae6ef7fcc742

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
