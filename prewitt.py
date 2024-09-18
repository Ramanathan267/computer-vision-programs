import cv2
import numpy as np
img = cv2.imread('C:/Users/Ramanathan/OneDrive/Pictures/Leaving Fingers.jpg', cv2.IMREAD_GRAYSCALE)

prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

grad_x = cv2.filter2D(img, cv2.CV_8U, prewitt_x)
grad_y = cv2.filter2D(img, cv2.CV_8U, prewitt_y)

grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

cv2.imshow('Prewitt Edge Detection', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
