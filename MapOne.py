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
TEXT_COLOR = (255, 255, 255)  # Color del texto

# Configuración de dimensiones del laberinto
CELL_SIZE = 20
PELLET_SIZE = 4
PACMAN_SIZE = 10

# Mapa de los niveles (1 = pared, 0 = camino con pellet)
level_1 = [
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

level_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

level_3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

levels = [level_1, level_2, level_3]  # Lista con los niveles
current_level = 0  # Nivel actual

# Inicialización de Pac-Man
pacman_position = [1, 1]  # Posición inicial


# dibujar el mapa
def draw_map():
    screen.fill(BLACK)  # Fondo negro

    for row in range(len(levels[current_level])):
        for col in range(len(levels[current_level][row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if levels[current_level][row][col] == 1:
                pygame.draw.rect(screen, WALL_COLOR, (x, y, CELL_SIZE, CELL_SIZE))  # Dibujar las paredes
            elif levels[current_level][row][col] == 0:
                pygame.draw.circle(screen, PELLET_COLOR, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), PELLET_SIZE)

    # Dibujar a Pac-Man
    pacman_x = pacman_position[1] * CELL_SIZE + CELL_SIZE // 2
    pacman_y = pacman_position[0] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, PACMAN_COLOR, (pacman_x, pacman_y), PACMAN_SIZE)


# Función para encontrar los vecinos válidos
def get_neighbors_with_weights(position):
    row, col = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(levels[current_level]) and 0 <= new_col < len(levels[current_level][0]):
            if levels[current_level][new_row][new_col] in [0, 2]:
                # El peso será 1 si hay un pellet, 2 si está vacío
                weight = 1 if levels[current_level][new_row][new_col] == 0 else 2
                neighbors.append((weight, (new_row, new_col)))

    return neighbors


# Función para comprobar si se han recogido todos los pellets
def check_all_pellets_collected():
    for row in range(len(levels[current_level])):
        for col in range(len(levels[current_level][row])):
            if levels[current_level][row][col] == 0:  # Si aún queda algun pellet
                return False
    return True


# Función para manejar el movimiento de PacMan
def move_pacman():
    global pacman_position

    # Inicialización para Prim
    visited = set()
    priority_queue = []
    start = tuple(pacman_position)

    # Agregar posición inicial
    heapq.heappush(priority_queue, (0, start, start))  # (peso, posición_actual, posición_anterior)
    next_move = None

    while priority_queue:
        weight, current, previous = heapq.heappop(priority_queue)

        if current not in visited:
            visited.add(current)

            # Si es el primer movimiento desde la posición inicial, guardarlo
            if previous == start and next_move is None:
                next_move = current

            # Si encontramos un pellet, movernos hacia él
            if levels[current_level][current[0]][current[1]] == 0:
                levels[current_level][current[0]][current[1]] = 2  # Marcar como recogido
                pacman_position = list(current)
                return

            # Agregar vecinos no visitados a la cola de prioridad
            for weight, neighbor in get_neighbors_with_weights(current):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, neighbor, current))

    # Si no encontramos pellets pero tenemos un siguiente movimiento válido
    if next_move:
        pacman_position = list(next_move)

# mostrar mensaje
def draw_text(text, position, font_size=30):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, position)


# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_pacman()  # Movimiento autónomo
    draw_map()  # Dibujar el mapa

    # Verificar si el nivel está completado
    if check_all_pellets_collected():
        if current_level < len(levels) - 1:  # Si no es el último nivel
            draw_text("Nivel Completado!", (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2), 40)
        else:  # Si es el último nivel
            draw_text("Juego Completado!", (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2), 40)

        pygame.display.flip()
        pygame.time.wait(1000)  # antes de pasar al siguiente nivel

        # Pasar al siguiente nivel
        current_level += 1
        if current_level >= len(levels):
            running = False  # Termina el juego
        pacman_position = [1, 1]  # Reiniciar posición de Pac-Man

    pygame.display.flip()  # Actualizar la pantalla
    clock.tick(5)  # Limitar la velocidad del juego

pygame.quit()
sys.exit()

