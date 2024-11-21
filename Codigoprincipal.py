

import numpy as np
import pygame
import graphlib 
import graphviz as gv
import tkinter as tk

# codigo principal(generar ventana)

    


pygame.init()
pygame.mixer.init()
text = pygame.font.SysFont('Arial',15)
pantalla = pygame.display.set_mode((700,500))
ancho = pantalla.get_width()
altura = pantalla.get_height()
pygame.display.set_caption("MENU")
pantalla.fill("BLACK")
menu = 0 # para poder cambiar de ventana
archivo_inicio = 'inicio-juego.mp3'
pygame.mixer.music.load(archivo_inicio)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
   pygame.time.Clock().tick(5)



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
    global menu
    menu +=1




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
#objetos#



boton(330,200,50,18,'Iniciar',sumar_menu,False)
#-------#


funcionando = True

while funcionando == True:

    pantalla.fill("BLACK")
    
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            funcionando = False
    if menu == 0:
     texto()

     for object in objetos:

            object.procesar()


    elif menu == 1:

        pantalla.fill("BLACK")



    



        


    
    
                

       

           
           
    





    pygame.display.update()


pygame.quit()