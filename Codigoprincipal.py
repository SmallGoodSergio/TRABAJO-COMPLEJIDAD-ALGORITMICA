

import numpy as np
import pygame
import graphlib 
import graphviz as gv
import tkinter as tk



# codigo principal(generar ventana)


    


pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((700,500))
ancho = pantalla.get_width()
altura = pantalla.get_height()
pygame.display.set_caption("MENU")
pantalla.fill("BLACK")

archivo_inicio = 'inicio-juego.mp3'
pygame.mixer.music.load(archivo_inicio)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
   pygame.time.Clock().tick(5)





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



# -----------------------------------#
#------------------------------------#

#colores#

def colores(n):

 if n == 1:

    gris = (155,155,155)
    return gris
 elif n == 2:

    negro = (0,0,0)
    return negro


#-------#

funcionando = True

while funcionando == True:

    texto()
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            funcionando = False
    

    # conseguir la posicion del mouse#
    mouse = pygame.mouse.get_pos()
    # -------------------------------#

    if 300 <= mouse[0] <=360 and 190 <=mouse[1] <=210:
       boton_efecto()

       pygame.draw.rect(pantalla,colores(1),[300,190,100,40])
    
    else: 

       pygame.draw.rect(pantalla,colores(2),[300,190,100,40])


    opcion_iniciar()
    pygame.display.update()


pygame.quit()