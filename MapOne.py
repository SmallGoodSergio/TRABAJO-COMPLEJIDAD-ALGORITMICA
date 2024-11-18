import pygame
import sys
import heapq

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
PACMAN_COLOR = (255, 255, 0)  # Color del Pac-Man

# Configuración de dimensiones del laberinto
CELL_SIZE = 20
PELLET_SIZE = 4
PACMAN_SIZE = 10

# Mapa del laberinto (1 = pared, 0 = camino con pellet)
map_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Inicialización de Pac-Man
pacman_position = [1, 1]  # Posición inicial (fila, columna)

# Función para dibujar el mapa
def draw_map():
    screen.fill(BLACK)  # Fondo negro

    for row in range(len(map_layout)):
        for col in range(len(map_layout[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if map_layout[row][col] == 1:
                pygame.draw.rect(screen, WALL_COLOR, (x, y, CELL_SIZE, CELL_SIZE))  # Dibujar las paredes
            elif map_layout[row][col] == 0:
                pygame.draw.circle(screen, PELLET_COLOR, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), PELLET_SIZE)

    # Dibujar a Pac-Man
    pacman_x = pacman_position[1] * CELL_SIZE + CELL_SIZE // 2
    pacman_y = pacman_position[0] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, PACMAN_COLOR, (pacman_x, pacman_y), PACMAN_SIZE)

# Función para encontrar los vecinos válidos para el Pac-Man
def get_neighbors(position):
    """Encuentra los vecinos válidos de una posición."""
    row, col = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Permitir movimiento en celdas vacías (2) y con pellets (0)
        if 0 <= new_row < len(map_layout) and 0 <= new_col < len(map_layout[0]):
            if map_layout[new_row][new_col] in [0, 2]:
                neighbors.append((new_row, new_col))

    return neighbors



# Movimiento autónomo basado en MST (Prim)
def move_pacman():
    global pacman_position

    # Usamos una prioridad basada en la distancia manhattan a los pellets
    priority_queue = []
    visited = set()
    start = tuple(pacman_position)

    # Añadimos la posición inicial
    heapq.heappush(priority_queue, (0, start))
    visited.add(start)

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        # Si encontramos un pellet, movernos a su dirección
        if map_layout[current[0]][current[1]] == 0:
            map_layout[current[0]][current[1]] = 2  # Marcar como vacío
            pacman_position = list(current)  # Avanzar paso a paso
            return  # Terminar el turno

        # Añadir vecinos a la cola de prioridad
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(priority_queue, (
                abs(neighbor[0] - pacman_position[0]) + abs(neighbor[1] - pacman_position[1]), neighbor))


# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_pacman()  # Movimiento autónomo del Pac-Man
    draw_map()  # Dibujar el mapa
    pygame.display.flip()  # Actualizar la pantalla
    clock.tick(5)  # Limitar la velocidad del juego

pygame.quit()
sys.exit()