import cv2

img = cv2.imread('C:/Users/Ramanathan/OneDrive/Pictures/Leaving Fingers.jpg', cv2.IMREAD_GRAYSCALE)

thresh_val = 127
_, thresh = cv2.threshold(img, thresh_val, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary Thresholding', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
