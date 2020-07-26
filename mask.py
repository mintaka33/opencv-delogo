import cv2
import numpy as np

img = cv2.imread('test.bmp')
print(img.shape)
(h, w, _) = img.shape

img_grey = cv2.imread('logo.bmp', cv2.IMREAD_GRAYSCALE)
print(img_grey.shape)
h2, w2 = img_grey.shape

img_binary = cv2.threshold(img_grey, 128, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('bin.bmp', img_binary)

mask = np.zeros((h, w), np.uint8)
mask[50:50+h2, 50:50+w2] = img_binary
cv2.imwrite('tmp.bmp', mask)

#cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)



#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gaussian_blur = cv2.GaussianBlur(img, (5,5), sigmaX=0)
#edges = cv2.Canny(gaussian_blur, 100, 200)
#cv2.imshow('edge', edges)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

