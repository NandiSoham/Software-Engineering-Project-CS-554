import cv2
import numpy as np

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Get the height and width of the frame
    height, width, _ = frame.shape

    # Define the size and position of the three boxes
    box_height = int(height / 3)
    top_boxes = frame[:2*box_height, :]
    bottom_box = frame[2*box_height:, :]

    # Draw green borders around the boxes
    frame = cv2.rectangle(frame, (0, 0), (width, 2*box_height), (0, 255, 0), 2)
    frame = cv2.rectangle(frame, (0, 2*box_height), (width, height), (0, 255, 0), 2)

    # Show the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
