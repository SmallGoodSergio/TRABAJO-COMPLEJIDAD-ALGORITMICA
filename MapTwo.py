import pygame
import sys
import numpy as np
import time
import random
import graphviz as gv
from collections import defaultdict

# Inicialización de pygame
pygame.init()

# Configuración del tamaño de la ventana
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")
text = pygame.font.SysFont('Arial',15)
imagen = pygame.image.load("pacman_2.png")
matriz = np.loadtxt("texto.txt",dtype=int)
tamaño_celda = 20 # tamaño de cada pedazo de pared
imagen = pygame.transform.scale(imagen,(15,15))
# Colores del mapa
BLACK = (0, 0, 0)  # Fondo del mapa
WALL_COLOR = (0, 0, 139)  # Color de las paredes
PELLET_COLOR = (255, 182, 193)  # Color para los pellets
GRIS = (128,128,128) # color para espacio aparte
pos_per = [100,100]
altura_pared = 4  # altura de la pared
distancia = list() # listado para las distancias
VERDE_OSCURO = (1,50,32) # color para espacio de botones
bolas = list() #lista de bolas

#clases#


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
        self.presionado_anterior = False

        self.superficie = pygame.Surface((self.ancho,self.altura)) #crea una superficie propia para el boton
        self.rectangulo = pygame.Rect(self.x,self.y,self.ancho,self.altura) #crea el rectangulo

        self.texto = text.render(textoboton,True,GRIS)


        self.color = { #diccionario para acceder a los colores


            'normal': '#FFFF00',
            'hover' : '#666666',
            'presionado':'#333333',
        }
        objetos.append(self)


    def procesar(self):

        posicionmouse = pygame.mouse.get_pos()
        mouse_presionado = pygame.mouse.get_pressed(num_buttons=3)[0]
        self.superficie.fill(self.color['normal'])

        if self.rectangulo.collidepoint(posicionmouse):

            self.superficie.fill(self.color['hover'])
            if  mouse_presionado and not self.presionado_anterior:
                self.superficie.fill(self.color['presionado'])

                self.clickfuncion()
        
        

                    
                
            

        self.presionado_anterior = mouse_presionado
        

        self.superficie.blit(self.texto,(10,0))

        screen.blit(self.superficie,self.rectangulo)

class Heap():
 
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []
 
    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode
 
    # Una función de utilidad para intercambiar dos nodos de
    # mínimo. Necesario para min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t
 
    # Una función estándar para acumular en un idx dado
    # Esta función también actualiza la posición de los nodos
    # cuando se intercambian. Se necesita puesto
    # para disminuirClave()
    # Position is needed for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
 
        if left < self.size and self.array[left][1] < \
                                self.array[smallest][1]:
            smallest = left
 
        if right < self.size and self.array[right][1] < \
                                self.array[smallest][1]:
            smallest = right
 
        # Los nodos que se intercambiarán en el montón mínimo
        # si idx no es el más pequeño
        if smallest != idx:
 
            # Intercambiar posiciones
            self.pos[ self.array[smallest][0] ] = idx
            self.pos[ self.array[idx][0] ] = smallest
 
            # Intercambiar nodos
            self.swapMinHeapNode(smallest, idx)
 
            self.minHeapify(smallest)
 
    # Función estándar para extraer el nodo mínimo del heap
    def extractMin(self):
 
        # Devuelve NULL si el montón está vacío
        if self.isEmpty() == True:
            return
 
        # Almacenar el nodo raíz
        root = self.array[0]
 
        # Reemplazar el nodo raíz con el último nodo
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
 
        # Actualizar posición del último nodo
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
 
        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)
 
        return root
 
    def isEmpty(self):
        return True if self.size == 0 else False
 
    def decreaseKey(self, v, dist):
 
        # Get the index of v in  heap array
 
        i = self.pos[v]
 
        # Get the node and update its dist value
        self.array[i][1] = dist
 
        # Travel up while the complete tree is not
        # hepified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < \
                    self.array[(i - 1) // 2][1]:
 
            # Swap this node with its parent
            self.pos[ self.array[i][0] ] = (i-1)/2
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swapMinHeapNode(i, (i - 1)//2 )
 
            # move to parent index
            i = (i - 1) // 2;
 
    # A utility function to check if a given vertex
    # 'v' is in min heap or not
    def isInMinHeap(self, v):
 
        if self.pos[v] < self.size:
            return True
        return False


def printArr(parent, n):
    for i in range(1, n):
        print("% d - % d" % (parent[i], i))




class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
 
    # Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):
 
        # Add an edge from src to dest.  A new node is
        # added to the adjacency list of src. The node
        # is added at the beginning. The first element of
        # the node has the destination and the second
        # elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)
 
        # Since graph is undirected, add an edge from
        # dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)
 
    # The main function that prints the Minimum
    # Spanning Tree(MST) using the Prim's Algorithm.
    # It is a O(ELogV) function
    def PrimMST(self):
        # Get the number of vertices in graph
        V = self.V 
         
        # key values used to pick minimum weight edge in cut
        key = []  
         
        # List to store constructed MST
        parent = []
 
        # minHeap represents set E
        minHeap = Heap()
 
        # Initialize min heap with all vertices. Key values of all
        # vertices (except the 0th vertex) is is initially infinite
        for v in range(V):
            parent.append(-1)
            key.append(1e7)
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) )
            minHeap.pos.append(v)
 
        # Make key value of 0th vertex as 0 so
        # that it is extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])
 
        # Initially size of min heap is equal to V
        minHeap.size = V;
 
        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while minHeap.isEmpty() == False:
 
            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
 
            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:
 
                v = pCrawl[0]
 
                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u
 
                    # update distance value in min heap also
                    minHeap.decreaseKey(v, key[v])
 
        printArr(parent, V)
# =========================#


# definir funciones ------ # 
def colocar(colocador):


    x = colocador[0]
    y = colocador[1]


    pygame.draw.circle(screen,PELLET_COLOR,(x,y),4)
    bolas.append((x,y))

    print(f"posicion bolas = {bolas}")
    print(len(bolas))



def dibujar(lista):

    for n in range(len(lista)):

        pygame.draw.circle(screen,PELLET_COLOR,(lista[n][0],lista[n][1]),4)

def dibujar2(lista):

    for n in range(len(lista)):

     pygame.draw.rect(screen,WALL_COLOR,(lista[n][0],lista[n][1],10,altura_pared))

def dibujar3_in(imag,pos):

 screen.blit(imag,(pos[0],pos[1]))


def dibujar3_lu(imag,pos):
 clock = pygame.time.Clock()
 screen.fill("BLACK")
 screen.blit(imag,(pos[0],pos[1]))
 rect = pygame.Rect(pos[0], pos[1], imag.get_width(), imag.get_height())
 pygame.display.update(rect)
 



def espacioarbol():


    pygame.draw.rect(screen,GRIS,(800,0,1200,700))




def dibujar_matriz(arr):




   a = arr.shape[1]
   b = arr.shape[0]
   pared = [0] * 1
   n = 0
   for filas in range(b):
      
      for columnas in range(a):
            x = columnas * tamaño_celda
            y = filas * tamaño_celda
            
            if matriz[filas][columnas] == 1:
              pared[n] = pygame.draw.rect(screen, WALL_COLOR, (x, y, tamaño_celda, tamaño_celda))  # Dibujar las paredes
            
            pared.append(0)
            n+=1
            

      



def moverse(arr1,inicio,imag):
   bolas_restantes = arr1.copy()
   seguido = list()
   n = 0
   distancia = [0]*1
   
   while bolas_restantes:
      distancia[n] = 0
      seguir = random.choice(bolas_restantes)
      while inicio[0] != seguir[0] or inicio[1] != seguir[1]:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
            pygame.quit()
            exit()



        if inicio[0] > seguir[0]:

         inicio[0] -=1
         print(inicio)
         distancia[n] +=1
        
    
        elif inicio[0] < seguir[0]:

         inicio[0] +=1
         print(bolas_restantes)
        
         distancia[n] +=1


        if inicio[1] > seguir[1]:
       
         inicio[1] -=1
         distancia[n] +=1


        elif inicio[1] < seguir[1]:
        
         inicio[1]+=1
         distancia[n] +=1

        
        screen.fill("BLACK")  # Limpiar pantalla
        dibujar(bolas)  # Redibujar los puntos
        dibujar3_in(imag, inicio)  # Dibujar la imagen en movimiento
        espacioarbol()  # Redibujar el espacio del árbol
        espacio_botones()  # Redibujar el espacio de botones
        pygame.display.flip()  # Actualizar la pantalla



        print(f"distancia {n + 1} = {distancia[n]}")
      distancia.append(0)
      n+=1






    

    

    
      print(inicio)

      bolas_restantes.remove(seguir)



   


def crecer(arr):

    global altura_pared
    ultimo = len(arr)-1
    altura_pared +=20
    print(altura_pared)


def disminuir():
    global altura_pared
    altura_pared -= 20
def espacio_botones():
    pygame.draw.rect(screen,VERDE_OSCURO,(0,500,800,700))
    boton(130,650,50,18,'Disminuir',disminuir,False)


boton_crecer = boton(130,600,50,18,'Crecer',crecer,False)
boton_empezar = boton(200,600,80,20,'Empezar',lambda: moverse(bolas,pos_per,imagen),False)






    


# ============================== #








# Bucle principal del juego
running = True

while running:

    mouse = pygame.mouse.get_pos()

    screen.fill("BLACK")
    espacioarbol()
    espacio_botones()
    dibujar(bolas)
    dibujar3_in(imagen,pos_per)
    dibujar_matriz(matriz)
    boton_crecer.procesar()
    boton_empezar.procesar()


    if pygame.mouse.get_pressed(num_buttons=3)[0]:
      if mouse[1] >= 500 or 800 <= mouse[0]:
        print("no se puede colocar acá")
        time.sleep(0.2)
      else:
        colocar(mouse)
        time.sleep(0.5)
    
    if pygame.mouse.get_pressed(num_buttons=3)[1]:

        time.sleep(0.5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()
sys.exit()