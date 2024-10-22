import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Tamaño de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dibujo de Formas y Texto en Pygame")

# Colores
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Fuente de texto
fuente = pygame.font.SysFont(None, 55)

# Ciclo principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar la ventana
    ventana.fill(BLANCO)

    # Dibujar un rectángulo
    pygame.draw.rect(ventana, VERDE, (150, 150, 200, 100))

    # Dibujar un círculo
    pygame.draw.circle(ventana, AZUL, (400, 300), 75)

    # Renderizar texto
    texto = fuente.render("Hola, Pygame!", True, AZUL)
    ventana.blit(texto, (250, 500))

    # Actualizar la ventana
    pygame.display.flip()