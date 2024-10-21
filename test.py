import cv2

img = cv2.imread('dataset/fernando/rostro10.jpg',0)
umbral = 100     

_ , imgBin = cv2.threshold(img, umbral ,255, cv2.THRESH_BINARY)

cv2.imshow('binaria', imgBin)
cv2.waitKey(0)                   
cv2.destroyWindow('binaria')  