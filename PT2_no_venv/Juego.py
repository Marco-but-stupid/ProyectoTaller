import pygame
import math
import os
import time
import random

pygame.font.init() #inicializa las fuentes de texto en pygame

#Se crea la pantalla
ANCHO, ALTO = 1000, 667
VEN = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PT2")

#Se cargan las imágenes
NAVE_JUGADOR = pygame.image.load("Arcadia.png")
PROYECTIL = pygame.image.load("test_asteroid.png")

#Fondo
BG = pygame.image.load("Fondo.png")

#Sonido de fondo
pygame.mixer.init()  # Inicializa mixer
pygame.mixer.music.load("Background.mp3")  # Agrega música al juego
pygame.mixer.music.play(-1)  # Inicia la música al juego y "-1" lo vuelve a repetir en bucle


#Clase nave
class Objeto:
    def __init__(self, x, y, vida=60):
        self.x = x
        self.y = y
        self.vida = vida
        self.objeto_img = None

    #e: self, donde se debe dibujar la nave
    #s: la nave dibujada
    #r: -
    def dibujar(self, ventana):
        VEN.blit(self.objeto_img, (self.x, self.y))

    #e: self, donde se debe borrar el objeto
    #s: borra algún objeto de la ventana
    #r: -
    def borrar(self, ventana):
        VEN.blit(self.objeto_img, (999999, 999999))

class Jugador(Objeto):
    def __init__(self, x, y, vida=100):
        super().__init__(x, y, vida)    #permite heredar de la clase NAVE
        self.objeto_img = NAVE_JUGADOR
        self.mask = pygame.mask.from_surface(self.objeto_img)
        self.vida_max = vida

class Proyectil(Objeto):
    def __init__(self, x, y, vida=2):
        super().__init__(x, y, vida)    #permite heredar de la clase NAVE
        self.objeto_img = PROYECTIL
        self.mask = pygame.mask.from_surface(self.objeto_img)

    def movimiento(self, velx, vely):   #movimiento del proyectil
        self.x += velx
        self.y += vely

def main():     #función principal del juego

    jugador = Jugador(450, 557)

    CORRER = True
    FPS = 60    #veces por segundo que se corre el loop
    NIVEL = 0   #varible que permite cambiar de niveles
    VIDA = 60   #vida total del jugador, cada "vida" tiene 20 puntos

    # las fuente a utilizarse en el juego
    FUENTE_PRINCIPAL = pygame.font.SysFont("comicsans", 50)
    FUENTE_PERDER = pygame.font.SysFont("comicsans", 200)

    proyectiles = []    #lista con los proyectiles del nivel
    largo_nivel = 0     #cantidad de proyectiles en cada nivel

    velx = random.randint(-11, 11)  #velocidad horizontal del proyectil
    vely = random.randint(1, 11)    #velocidad horizontal del proyectil

    jugador_velocidad = 7.5   #velocidad de la nave

    #velocidades verticales y horizontales del proyectil
    proyectil_velocidad_x = random.randint(-8, 8)
    proyectil_velocidad_y = random.randint(1, 8)

    RELOJ = pygame.time.Clock() #mide el tiempo del juego

    terminar = False
    terminar_contador = 0

    def redibujar_ventana():    #función que actualiza la ventana en cada loop
        VEN.blit(BG, (0,0))
        Time = pygame.time.get_ticks() / 1000
        Contador = 0
        Score = 0

        VIDA_label = FUENTE_PRINCIPAL.render(f"Vida: {VIDA}",1 , (0, 0, 0))
        NIVEL_label = FUENTE_PRINCIPAL.render(f"Nivel: {NIVEL}", 1, (0, 0, 0))

        VEN.blit(VIDA_label, (50, 610))
        VEN.blit(NIVEL_label, (800, 610))


        if Contador or Score == Time:
            Contador += 1
            Score += 1
            print(Time)
            
        ContadorTiempo_label = FUENTE_PRINCIPAL.render(("Tiempo: " + str(Time)), 1, (0,0,0))
        VEN.blit(ContadorTiempo_label, (500, 610))
        
        Puntaje_label = FUENTE_PRINCIPAL.render(("Puntaje: " + str(Time)), 1, (0,0,0))
        VEN.blit(Puntaje_label, (200, 610))


        for proyectil in proyectiles:   #dibuja los proyectiles sobre la ventana
            proyectil.dibujar(VEN)

        jugador.dibujar(VEN)            #dibuja la nave sobre la ventana


        if terminar:
            terminar_label = FUENTE_PERDER.render("GAME OVER", 1, (255, 0, 0))
            VEN.blit(terminar_label, (73, 250))



        pygame.display.update()         #actualiza la pantalla del juego
        
    #loop del juego
    while CORRER:
        RELOJ.tick(FPS)

        redibujar_ventana()

        if VIDA < 1 or NIVEL > 3:
            terminar = True
            terminar_contador += 1
        if terminar:
            if terminar_contador > 240:
                CORRER = False
            else:
                continue

        if len(proyectiles) == 0:
            NIVEL += 1
            largo_nivel += 1
            for i in range(largo_nivel):
                proyectil = Proyectil(random.randint(100, 900), random.randint(10, 30))
                proyectiles.append(proyectil)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CORRER = False

        #permite el movimiento del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador.x - jugador_velocidad > 0:   #mueve la nave a la izquierda
            jugador.x -= jugador_velocidad
        if teclas[pygame.K_RIGHT] and jugador.x + jugador_velocidad + 100 < ANCHO:  #mueve la nave a la derecha
            jugador.x += jugador_velocidad
        if teclas[pygame.K_UP] and jugador.y - jugador_velocidad > 0:  #mueve la nave hacia arriba
            jugador.y -= jugador_velocidad
        if teclas[pygame.K_DOWN] and jugador.y + jugador_velocidad + 100 < ALTO:  #mueve la nave hacia abajo
            jugador.y += jugador_velocidad

        #permite el movimiento de los proyectiles
        for proyectil in proyectiles:

            proyectil.x += proyectil_velocidad_x
            proyectil.y += proyectil_velocidad_y

            if proyectil.x <= 0:
                proyectil_velocidad_x = -proyectil_velocidad_x
            elif proyectil.x >= 950:
                proyectil_velocidad_x = -proyectil_velocidad_x
            elif proyectil.y <= -10:
                proyectil_velocidad_y = -proyectil_velocidad_y
            elif proyectil.y >= 600:
                proyectil_velocidad_y = -proyectil_velocidad_y

        if math.sqrt(math.pow(proyectil.x - jugador.x, 2) + math.pow(proyectil.y - jugador.y, 2)) < 75:
            VIDA -= 1
            proyectiles.remove(proyectil)

main()
