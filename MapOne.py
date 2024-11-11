import pygame
import sys

# Inicialización de pygame
pygame.init()

# Configuración del tamaño de la ventana
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Colores del mapa
BLACK = (0, 0, 0)  # Fondo del mapa
WALL_COLOR = (0, 0, 139)  # Color de las paredes
PELLET_COLOR = (255, 182, 193)  # Color para los pellets

# Configuración de dimensiones del laberinto
CELL_SIZE = 20
PELLET_SIZE = 4

