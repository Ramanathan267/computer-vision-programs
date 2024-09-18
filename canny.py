import cv2
img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
