import cv2
import numpy as np

def create_color_detection_window():
    cv2.namedWindow('Color Detection')
    cv2.createTrackbar('Hue', 'Color Detection', 0, 179, on_trackbar_change)
    cv2.createTrackbar('Saturation', 'Color Detection', 0, 255, on_trackbar_change)
    cv2.createTrackbar('Value', 'Color Detection', 0, 255, on_trackbar_change)

def on_trackbar_change(x):
    pass

def get_color_mask(hue, saturation, value, frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_color = np.array([hue, saturation, value], dtype=np.uint8)
    upper_color = np.array([180, 255, 255], dtype=np.uint8)  

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

        hue = cv2.getTrackbarPos('Hue', 'Color Detection')
        saturation = cv2.getTrackbarPos('Saturation', 'Color Detection')
        value = cv2.getTrackbarPos('Value', 'Color Detection')
        frame = np.flip(frame, axis=1)
        result = get_color_mask(hue, saturation, value, frame)

        cv2.imshow('Color Detection', result)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
