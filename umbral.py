import cv2 as cv

img = cv.imread('C:/Users/Ferlo/Desktop/IA/f1.jpg', 1)
rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB)
hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)

umbralBajo=(40, 30, 0)
umbralAlto=(80, 255, 255)
# umbralBajoB=(170, 50, 0)
# umbralAltoB=(180, 255, 255)


mascara1 = cv.inRange(hsv, umbralBajo, umbralAlto)
# mascara2 = cv.inRange(hsv, umbralBajoB, umbralAltoB)

# mascara = mascara1 + mascara2

resultado = cv.bitwise_and(img, img, mask=mascara1)

cv.imshow('resultado', resultado)
#cv.imshow('mascara', mascara)
cv.imshow('img',img)
#cv.imshow('rgb', rgb)
#cv.imshow('hsv', hsv)

cv.waitKey(0)
cv.destroyAllWindows()