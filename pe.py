import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Colores
BLACK = (0, 0, 0)
WALL_COLOR = (0, 0, 139)
PELLET_COLOR = (255, 182, 193)
PACMAN_COLOR = (255, 255, 0)

# Mapa del nivel (1 = pared, 0 = pellet)
level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Posición inicial de Pac-Man
pacman_x = 1
pacman_y = 1

# Velocidad de Pac-Man
dx, dy = 0, 0

# Función para dibujar el mapa
def draw_map():
    screen.fill(BLACK)
    for row in range(len(level)):
        for col in range(len(level[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if level[row][col] == 1:  # Pared
                pygame.draw.rect(screen, WALL_COLOR, (x, y, CELL_SIZE, CELL_SIZE))
            elif level[row][col] == 0:  # Pellet
                pygame.draw.circle(screen, PELLET_COLOR, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), 5)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = -1, 0
            elif event.key == pygame.K_DOWN:
                dx, dy = 1, 0
            elif event.key == pygame.K_LEFT:
                dx, dy = 0, -1
            elif event.key == pygame.K_RIGHT:
                dx, dy = 0, 1

    # Movimiento de Pac-Man
    new_x = pacman_x + dx
    new_y = pacman_y + dy

    if level[new_x][new_y] != 1:  # Evitar atravesar paredes
        pacman_x, pacman_y = new_x, new_y

    # Comer pellet
    if level[pacman_x][pacman_y] == 0:
        level[pacman_x][pacman_y] = 2  # Pellet recogido

    # Dibujar todo
    draw_map()
    pygame.draw.circle(
        screen,
        PACMAN_COLOR,
        (pacman_y * CELL_SIZE + CELL_SIZE // 2, pacman_x * CELL_SIZE + CELL_SIZE // 2),
        CELL_SIZE // 2,
    )
    pygame.display.flip()

    # Control de velocidad
    clock.tick(10)

pygame.quit()
sys.exit()
