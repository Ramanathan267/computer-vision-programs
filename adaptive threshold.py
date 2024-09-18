import cv2

img = cv2.imread('C:/Users/Ramanathan/OneDrive/Pictures/Leaving Fingers.jpg', cv2.IMREAD_GRAYSCALE)

thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Adaptive Thresholding', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
