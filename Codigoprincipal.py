

import numpy as np
import pygame
import graphlib 
import graphviz as gv
import tkinter as tk



# codigo principal(generar ventana)


    


pygame.init()
pantalla = pygame.display.set_mode((700,500))
ancho = pantalla.get_width()
altura = pantalla.get_height()
pygame.display.set_caption("MENU")
pantalla.fill("BLACK")



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


# -----------------------------------#
#------------------------------------#



funcionando = True

while funcionando == True:

    texto()
    opcion_iniciar()
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            funcionando = False
    
    pygame.display.update()

    # conseguir la posicion del mouse#
    mouse = pygame.mouse.get_pos()
    # -------------------------------#

    if 350 <= mouse[0] <=360 and 200 <=mouse[1] <=210:
       
       print("hola")



pygame.quit()