import cv2
import numpy as np

img = cv2.imread('C:/Users/Ramanathan/OneDrive/Pictures/image.webp', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)

top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('Top Hat', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
