import numpy as np
import cv2 as cv
import math 
#import a pre-trained file using haarcascades
rostro = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    #using gray scale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #detect multiple faces
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in rostros:
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5)
    cv.imshow('rostros', frame)
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
