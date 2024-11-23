

import numpy as np
import pygame
import graphlib 
import graphviz as gv
import tkinter as tk
import sys
import heapq
# codigo principal(generar ventana)

    


pygame.init()
pygame.mixer.init()
text = pygame.font.SysFont('Arial',15)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
pantalla = pygame.display.set_mode((700,500))
ancho = pantalla.get_width()
altura = pantalla.get_height()
pygame.display.set_caption("MENU")
pantalla.fill("BLACK")
menu = 0 # para poder cambiar de ventana
archivo_inicio = 'inicio-juego.mp3'
pygame.mixer.music.load(archivo_inicio)
pygame.mixer.music.play()
# Colores del mapa
BLACK = (0, 0, 0)  # Fondo del mapa
WALL_COLOR = (0, 0, 139)  # Color de las paredes
PELLET_COLOR = (255, 182, 193)  # Color para los pellets
PACMAN_COLOR = (255, 255, 0)  # Color del Pac-Man
TEXT_COLOR = (255, 255, 255)  # Color del texto
funcionando = True
funcionando2 = False
# Configuración de dimensiones del laberinto
CELL_SIZE = 20
PELLET_SIZE = 4
PACMAN_SIZE = 10
while pygame.mixer.music.get_busy():
   pygame.time.Clock().tick(5)




#=====================================================#

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
#============================#
# botones#
objetos = []
class boton:

    def __init__(self,x,y,ancho,altura,textoboton = "boton",clickfuncion = None, presionado = False):


        self.x = x
        self.y = y
        self.ancho = ancho
        self.altura = altura
        self.clickfuncion = clickfuncion
        self.presionado = presionado
        self.yapresionado = False

        self.superficie = pygame.Surface((self.ancho,self.altura)) #crea una superficie propia para el boton
        self.rectangulo = pygame.Rect(self.x,self.y,self.ancho,self.altura) #crea el rectangulo

        self.texto = text.render(textoboton,True,colores(1))


        self.color = { #diccionario para acceder a los colores


            'normal': '#000000',
            'hover' : '#666666',
            'presionado':'#333333',
        }
        objetos.append(self)


    def procesar(self):

        posicionmouse = pygame.mouse.get_pos()

        self.superficie.fill(self.color['normal'])

        if self.rectangulo.collidepoint(posicionmouse):

            self.superficie.fill(self.color['hover'])
            boton_efecto()
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.superficie.fill(self.color['presionado'])

                if self.presionado:
                    self.clickfuncion()
                elif not self.yapresionado:

                    self.clickfuncion()
                    self.yapresionado = True
                    
                
            
            else:
                self.yapresionado = False
        

        self.superficie.blit(self.texto,(10,0))

        pantalla.blit(self.superficie,self.rectangulo)


        
       
       




#--------#



# funciones antes del codigo principal #


def texto():

 f = pygame.font.SysFont('timesnewroman',30)
 blanco = (255,255,255)
 t = f.render('PACMAN',True,blanco)
 t2 = t.get_rect()
 t2.center = (350,50)
 pantalla.blit(t,t2)


def opcion_iniciar():
 f = pygame.font.SysFont('timesnewroman',15)
 blanco = (255,255,255)
 t = f.render('INICIAR',True,blanco)
 t2 = t.get_rect()
 t2.center = (350,200)
 pantalla.blit(t,t2)


def boton_efecto():

    archivo = 'boton-sonido.mp3'
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()
    pygame.event.wait()

def sumar_menu():
    global funcionando
    global running
    funcionando = False
    running = True


# dibujar el mapa
def draw_map():
    pantalla.fill(BLACK)  # Fondo negro

    for row in range(len(levels[current_level])):
        for col in range(len(levels[current_level][row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if levels[current_level][row][col] == 1:
                pygame.draw.rect(pantalla, WALL_COLOR, (x, y, CELL_SIZE, CELL_SIZE))  # Dibujar las paredes
            elif levels[current_level][row][col] == 0:
                pygame.draw.circle(pantalla, PELLET_COLOR, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), PELLET_SIZE)

    # Dibujar a Pac-Man
    pacman_x = pacman_position[1] * CELL_SIZE + CELL_SIZE // 2
    pacman_y = pacman_position[0] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(pantalla, PACMAN_COLOR, (pacman_x, pacman_y), PACMAN_SIZE)


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
    pantalla.blit(text_surface, position)


# Bucle principal del juego
running = True
clock = pygame.time.Clock()
#colores#

def colores(n):

 if n == 1:

    gris = (155,155,155)
    return gris
 elif n == 2:

    negro = (0,0,0)
    return negro


#-------#
#objetos#



boton(330,200,50,18,'Iniciar',sumar_menu,False)
#-------#

running = False
funcionando = True
while funcionando == True:

    pantalla.fill("BLACK")
    
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            funcionando = False

    texto()

    for object in objetos:

            object.procesar()

    pygame.display.update()

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


