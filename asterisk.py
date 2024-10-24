import pygame
import math

# Configuraciones iniciales para Pygame
ANCHO_VENTANA = 800
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ANCHO_VENTANA))
pygame.display.set_caption("Visualización de Nodos")

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NARANJA = (255, 165, 0)
PURPURA = (128, 0, 128)

class Nodo:
    def __init__(self, fila, col, ancho, total_filas):
        self.fila = fila
        self.col = col
        self.x = fila * ancho
        self.y = col * ancho
        self.color = BLANCO
        self.ancho = ancho
        self.total_filas = total_filas
        self.g = 0
        self.h = 0
        self.f = 0
        self.Padre = None
        self.bloqueado = False

    def get_pos(self):
        return self.fila, self.col

    def es_pared(self):
        return self.color == NEGRO

    def es_inicio(self):
        return self.color == NARANJA

    def es_fin(self):
        return self.color == PURPURA

    def restablecer(self):
        self.color = BLANCO
        self.bloqueado = False

    def hacer_inicio(self):
        self.color = NARANJA

    def hacer_pared(self):
        self.color = NEGRO
        self.bloqueado = True

    def hacer_fin(self):
        self.color = PURPURA

    def hacer_camino(self):
        self.color = VERDE

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))

def crear_grid(filas, ancho):
    grid = []
    ancho_nodo = ancho // filas
    for i in range(filas):
        grid.append([])
        for j in range(filas):
            nodo = Nodo(i, j, ancho_nodo, filas)
            grid[i].append(nodo)
    return grid

def dibujar_grid(ventana, filas, ancho):
    ancho_nodo = ancho // filas
    for i in range(filas):
        pygame.draw.line(ventana, GRIS, (0, i * ancho_nodo), (ancho, i * ancho_nodo))
        for j in range(filas):
            pygame.draw.line(ventana, GRIS, (j * ancho_nodo, 0), (j * ancho_nodo, ancho))

def dibujar(ventana, grid, filas, ancho):
    ventana.fill(BLANCO)
    for fila in grid:
        for nodo in fila:
            nodo.dibujar(ventana)

    dibujar_grid(ventana, filas, ancho)
    pygame.display.update()

def obtener_click_pos(pos, filas, ancho):
    ancho_nodo = ancho // filas
    y, x = pos
    fila = y // ancho_nodo
    col = x // ancho_nodo
    return fila, col

def heuristica(nodo1, nodo2):
    x1, y1 = nodo1.get_pos()
    x2, y2 = nodo2.get_pos()
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def reconstruir_camino(came_from, nodo_actual, dibujar):
    while nodo_actual in came_from:
        nodo_actual = came_from[nodo_actual]
        nodo_actual.hacer_camino()
        dibujar()

def algoritmo(grid, start, end, dibujar):
    conocidos = []
    conocidos.append(start)

    came_from = {}

    start.g = 0
    start.f = heuristica(start, end)

    while len(conocidos) > 0:
        # Ordenamos los nodos conocidos por el valor de f
        conocidos.sort(key=lambda nodo: nodo.f)

        nodo_actual = conocidos.pop(0)

        if nodo_actual == end:
            reconstruir_camino(came_from, end, dibujar)
            end.hacer_fin()
            return True

        vecinos = [
            (nodo_actual.fila - 1, nodo_actual.col),  # Arriba
            (nodo_actual.fila + 1, nodo_actual.col),  # Abajo
            (nodo_actual.fila, nodo_actual.col - 1),  # Izquierda
            (nodo_actual.fila, nodo_actual.col + 1)   # Derecha
        ]

        for fila, col in vecinos:
            if 0 <= fila < len(grid) and 0 <= col < len(grid[0]):
                vecino = grid[fila][col]

                if vecino.bloqueado:
                    continue

                temp_g_score = nodo_actual.g + 1

                if temp_g_score < vecino.g or vecino not in conocidos:
                    vecino.g = temp_g_score
                    vecino.h = heuristica(vecino, end)
                    vecino.f = vecino.g + vecino.h
                    vecino.Padre = nodo_actual

                    if vecino not in conocidos:
                        conocidos.append(vecino)

        dibujar()

        if nodo_actual != start:
            nodo_actual.hacer_camino()

    return False

def main(ventana, ancho):
    FILAS = 10
    grid = crear_grid(FILAS, ancho)

    inicio = None
    fin = None

    corriendo = True

    while corriendo:
        dibujar(ventana, grid, FILAS, ancho)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            if pygame.mouse.get_pressed()[0]:  # Click izquierdo
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                if not inicio and nodo != fin:
                    inicio = nodo
                    inicio.hacer_inicio()

                elif not fin and nodo != inicio:
                    fin = nodo
                    fin.hacer_fin()

                elif nodo != fin and nodo != inicio:
                    nodo.hacer_pared()

            elif pygame.mouse.get_pressed()[2]:  # Click derecho
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                nodo.restablecer()
                if nodo == inicio:
                    inicio = None
                elif nodo == fin:
                    fin = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and inicio and fin:
                    for fila in grid:
                        for nodo in fila:
                            nodo.Padre = None

                    algoritmo(grid, inicio, fin, lambda: dibujar(ventana, grid, FILAS, ancho))

    pygame.quit()

main(VENTANA, ANCHO_VENTANA)
