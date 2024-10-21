import cv2 as cv
import numpy as np
import math

cap = cv.VideoCapture(0)
i = 0

while(True):
    ret,img = cap.read()
    img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img3 = cv.cvtColor(img2, cv.COLOR_RGB2HSV)
    if(ret == True):
        umbralBajo=(85, 150, 0)
        umbralAlto=(140, 255, 255)
        # umbralBajoB=(170, 150, 0)
        # umbralAltoB=(180, 255, 255)

        mascara = cv.inRange(img3, umbralBajo, umbralAlto)
        # mascara1 = cv.inRange(img3, umbralBajo, umbralAlto)
        # mascara2 = cv.inRange(img3, umbralBajoB, umbralAltoB)

        # mascara = mascara1 + mascara2

        resultado = cv.bitwise_and(img, img, mask=mascara)
        # Encontrar contornos en la máscara
        contours, _ = cv.findContours(mascara, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        # Si se encuentra al menos un contorno, seguir el objeto
        if contours:
            # Tomar el contorno más grande
            largest_contour = max(contours, key=cv.contourArea)
            
            # Encontrar el centro del contorno usando un círculo mínimo que lo rodee
            ((x, y), radius) = cv.minEnclosingCircle(largest_contour)
            
            # Dibujar el círculo y el centro en el frame original si el radio es mayor que un umbral
            if radius > 10:
                i=i+1
                cv.rectangle(resultado, (int(x-radius), int(y-radius)),(int(x+radius), int(y+radius)), (0, 255, 255),2)
                resultado2 = resultado[int(y-radius):int(y+radius), int(x-radius):int(x+radius)]
                cv.imwrite('/Users/Ferlo/Desktop/dataset/ex'+str(i)+'.jpg', resultado2)
        # Mostrar el frame
        cv.imshow('resultado', resultado)
        cv.imshow('mascara', mascara)
        cv.imshow('img',img)
        cv.imshow('img2', img2)
        cv.imshow('img3', img3)

        k=cv.waitKey(1) & 0xFF
        if(k == 27):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()