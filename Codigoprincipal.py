

import numpy as np
import pygame
import graphlib 
import graphviz as gv
import tkinter as tk



# codigo principal(generar ventana)


    


pygame.init()
pantalla = pygame.display.set_mode((700,500))

pygame.display.set_caption("MENU")
pantalla.fill("BLACK")



# funciones antes del codigo principal#

def texto():

 f = pygame.font.SysFont('timesnewroman',30)
 blanco = (255,255,255)
 t = f.render('PACMAN',True,blanco)
 t2 = t.get_rect()
 t2.center = (350,50)
 pantalla.blit(t,t2)

funcionando = True



# -----------------------------------#
while funcionando == True:

    texto()
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            funcionando = False
    
    pygame.display.update()

pygame.quit()