import cv2
import numpy as np

img = cv2.imread('C:/Users/Ramanathan/OneDrive/Pictures/Leaving Fingers.jpg', cv2.IMREAD_GRAYSCALE)

roberts_cross_v = np.array([[1, 0], [0, -1]])
roberts_cross_h = np.array([[0, 1], [-1, 0]])

vertical = cv2.filter2D(img, cv2.CV_8U, roberts_cross_v)
horizontal = cv2.filter2D(img, cv2.CV_8U, roberts_cross_h)

edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))

cv2.imshow('Robert Edge Detection', edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
