import cv2
umbral = 80
# Cargar la imagen desde un archivo
image = cv2.imread('dataset/fernando/rostro350.jpg', 0)

# Definir la escala en porcentaje (por ejemplo, 50%)
scale_percent = 80 

# Calcular las nuevas dimensiones
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
new_dim = (width, height)

# Redimensionar la imagen
resized_image = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)

_ , imgBin = cv2.threshold(resized_image, umbral ,255, cv2.THRESH_BINARY)



cv2.imshow('binaria', imgBin)
cv2.waitKey(0)
cv2.destroyAllWindows()