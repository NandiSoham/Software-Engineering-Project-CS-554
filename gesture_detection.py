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

    return result, mask

def identify_paper_position(mask, height):
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If no contours found, return None
    if not contours:
        return None

    # Find the contour with the largest area (the paper spot)
    max_contour = max(contours, key=cv2.contourArea)

    # Get the bounding rectangle of the paper spot
    x, y, w, h = cv2.boundingRect(max_contour)

    # Calculate the center of the paper spot
    center_x = x + w // 2

    # Determine if the center is on the left or right side
    if center_x < height // 2:
        return 'A'
    else:
        return 'B'

def main():
    cap = cv2.VideoCapture(0)
    create_color_detection_window()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        height, width, _ = frame.shape
        box_height = int(height / 3)

        hue = cv2.getTrackbarPos('Hue', 'Color Detection')
        saturation = cv2.getTrackbarPos('Saturation', 'Color Detection')
        value = cv2.getTrackbarPos('Value', 'Color Detection')

        result, mask = get_color_mask(hue, saturation, value, frame)

        # Identify the position of the colored paper
        position = identify_paper_position(mask, height)

        # Display the result and position
        cv2.imshow('Color Detection', result)
        print("Position:", position)

        frame = cv2.rectangle(frame, (0, 0), (width, 2 * box_height), (0, 255, 0), 2)
        frame = cv2.rectangle(frame, (0, 2 * box_height), (width, height), (0, 255, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
