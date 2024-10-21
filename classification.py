import cv2
import numpy as np
red_elements = 0
blue_elements =0
green_elements = 0
yellow_elements = 0

image = cv2.imread('salida.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
lower_redb = np.array([170, 120, 70])
upper_redb = np.array([180, 255, 255])

lower_green = np.array([36, 100, 100])
upper_green = np.array([86, 255, 255])

lower_yellow = np.array([26, 100, 100])
upper_yellow = np.array([35, 255, 255])

lower_blue = np.array([94, 80, 2])
upper_blue = np.array([126, 255, 255])

# Crear máscaras para cada color

mask_red1 = cv2.inRange(hsv, lower_red, upper_red)
mask_red2 = cv2.inRange(hsv, lower_redb, upper_redb)
mask_red = mask_red1 + mask_red2
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Encontrar los contornos para cada color
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original para cada color
for contour in contours_red:
    cv2.drawContours(image, [contour], -1, (0, 0, 255), 3)  # Rojo
    red_elements = red_elements + 1

for contour in contours_green:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 3)  # Verde
    green_elements = green_elements + 1

for contour in contours_yellow:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 3)  # Amarillo
    yellow_elements = yellow_elements + 1

for contour in contours_blue:
    cv2.drawContours(image, [contour], -1, (255, 0, 0), 3)  # Azul
    blue_elements = blue_elements + 1

# Mostrar la imagen con los objetos clasificados por color
cv2.imshow('Clasificación de colores', image)
print('')
cv2.waitKey(0)
cv2.destroyAllWindows()
