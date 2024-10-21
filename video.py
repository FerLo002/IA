import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(True):
    ret,img = cap.read()
    if(ret == True):
        cv.imshow('marco', img)
        x,y = img.shape[:2]
        img2 = np.zeros((x,y), dtype='uint8')

        # hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        # cv.imshow('hsv', hsv)
        b,g,r = cv.split(img)
        bm = cv.merge([b,img2, img2])
        gm = cv.merge([img2, g, img2])
        rm = cv.merge([img2, img2, r])

        cv.imshow('b', bm)
        cv.imshow('g', gm)
        cv.imshow('r', rm)

        k=cv.waitKey(1) & 0xFF
        if(k == 27):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()