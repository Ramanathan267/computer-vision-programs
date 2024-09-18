import cv2
import numpy as np

img = cv2.imread('original_image.jpg')

watermark = cv2.imread('watermark_image.png', cv2.IMREAD_GRAYSCALE)

watermark_resized = cv2.resize(watermark, (img.shape[1], img.shape[0]))


img_float = img.astype(np.float32)

watermarked_img = cv2.addWeighted(img_float, 1, watermark_resized, 0.5, 0)
watermarked_img = watermarked_img.astype(np.uint8)

cv2.imshow('Watermarked Image', watermarked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
