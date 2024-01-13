import cv2
import numpy as np
img = cv2.imread('red.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0,100,100])
upper = np.array([10,255,255])
mask = cv2.inRange(hsv_img,lower,upper)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_contour_area = 10
red_balls = []
for contour in contours:
    if cv2.contourArea(contour) > min_contour_area:
        red_balls.append(contour)
for contour in red_balls:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Red Ball Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()