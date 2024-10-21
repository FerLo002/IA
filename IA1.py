import cv2 as cv
import numpy as np

img = cv.imread("f1.jpg", 0)
print(img.shape)
x,y = img.shape
img2 = np.zeros((x*2,y*2), dtype='uint8')
for i in range(x):
    for j in range(y):
        img2[i*2,j*2] = img[i,j]

cv.imshow('marco', img)
cv.imshow('scalation', img2)
cv.waitKey(0)
cv.destroyAllWindows()

