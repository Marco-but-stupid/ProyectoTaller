import pygame
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

#Clase nave
class Objeto:
    def __init__(self, x, y, vida=60):
        self.x = x
        self.y = y
        self.vida = vida
        self.objeto_img = None

    #dibuja la nave sobre la ventana
    #e: self, donde se debe dibujar la nave
    #s: la nave dibujada
    #r:
    def dibujar(self, ventana):
        VEN.blit(self.objeto_img, (self.x, self.y))

class Jugador(Objeto):
    def __init__(self, x, y, vida=100):
        super().__init__(x, y, vida)    #permite heredar de la clase NAVE
        self.objeto_img = NAVE_JUGADOR
        self.mask = pygame.mask.from_surface(self.objeto_img)
        self.vida_max = vida

class Proyectil(Objeto):
    def __init__(self, x, y, vida=2):
        super().__init__(x, y, vida)
        self.objeto_img = PROYECTIL
        self.mask = pygame.mask.from_surface(self.objeto_img)

    def movimiento(self, velx, vely):
        self.x += velx
        self.y += vely

def main():
    CORRER = True
    FPS = 60  #veces por segundo que se corre el loop
    NIVEL = 0
    VIDA = 60
    FUENTE = pygame.font.SysFont("comicsans", 55)

    velx = random.randint(-8, 8)
    vely = random.randint(1, 8)

    jugador_velocidad = 7.5   #velocidad de la nave

    jugador = Jugador(450, 557)
    proyectil = Proyectil(460, 15)

    RELOJ = pygame.time.Clock()

    def redibujar_ventana():
        VEN.blit(BG, (0,0))
        VIDA_label = FUENTE.render(f"Vida: {VIDA}",1 , (0, 0, 0))
        NIVEL_label = FUENTE.render(f"Nivel: {NIVEL}", 1, (0, 0, 0))

        VEN.blit(VIDA_label, (50, 610))
        VEN.blit(NIVEL_label, (800, 610))

        proyectil.dibujar(VEN)
        jugador.dibujar(VEN)

        pygame.display.update() #actualiza la pantalla del juego

    while CORRER:
        RELOJ.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CORRER = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador.x - jugador_velocidad > 0:   #mueve la nave a la izquierda
            jugador.x -= jugador_velocidad
        if teclas[pygame.K_RIGHT] and jugador.x + jugador_velocidad + 100 < ANCHO:  #mueve la nave a la derecha
            jugador.x += jugador_velocidad
        if teclas[pygame.K_UP] and jugador.y - jugador_velocidad > 0:  #mueve la nave hacia arriba
            jugador.y -= jugador_velocidad
        if teclas[pygame.K_DOWN] and jugador.y + jugador_velocidad + 100 < ALTO:  #mueve la nave hacia abajo
            jugador.y += jugador_velocidad

        redibujar_ventana()

main()