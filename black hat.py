import cv2
import numpy as np

img = cv2.imread('C:/Users/Ramanathan/OneDrive/Pictures/Leaving Fingers.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Black Hat', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
