import cv2
import numpy as np
cap = cv2.VideoCapture('redd.mp4') 
if not cap.isOpened():
    print("Failed to open the video.")
else:
    print('done')
lower = np.array([0,100,100])
upper = np.array([10,255,255])
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_contour_area = 120
    red_balls = []
    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            red_balls.append(contour)
    for contour in red_balls:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Red Ball Detection', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()