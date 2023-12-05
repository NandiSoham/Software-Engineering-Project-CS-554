import cv2
import numpy as np
import mediapipe as mp
import time

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

def is_thumbs_down(hand_landmarks):
    # Check if the thumb is down (y-coordinate of the thumb tip is below the y-coordinate of the wrist)
    wrist_y = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.WRIST].y
    thumb_tip_y = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].y

    if thumb_tip_y > wrist_y:
        return True
    return False

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

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    thumbs_down_timer_start = None
    thumbs_down_duration = 5  # seconds

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

        # Use Mediapipe to detect hand gestures
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # Check if thumbs-down gesture is detected
        thumbs_down_detected = False
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if is_thumbs_down(hand_landmarks):
                    thumbs_down_detected = True
                    if thumbs_down_timer_start is None:
                        thumbs_down_timer_start = time.time()
                    else:
                        elapsed_time = time.time() - thumbs_down_timer_start
                        if elapsed_time >= thumbs_down_duration:
                            print("Thumbs Down for 5 seconds! Closing the camera.")
                            cap.release()
                            cv2.destroyAllWindows()
                            exit()
                else:
                    thumbs_down_timer_start = None

        # Display the result and position
        cv2.imshow('Color Detection', result)
        print("Position:", position)

        frame = cv2.rectangle(frame, (0, 0), (width, 2 * box_height), (0, 255, 0), 2)
        frame = cv2.rectangle(frame, (0, 2 * box_height), (width, height), (0, 255, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
