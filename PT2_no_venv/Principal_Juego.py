import pygame
import random
import math

#se inicializa pygame
pygame.init()

#se crea la pantalla
screen = pygame.display.set_mode((1000, 667))
DiedImg = pygame.image.load("Died.png")

#Fondo del juego
fondo = pygame.image.load("Fondo.png")

#Título e ícono
pygame.display.set_caption("Mars approach")
icono = pygame.image.load("Marte.png")
pygame.display.set_icon(icono)

#Jugador
jugadorImg = pygame.image.load("Arcadia.png")
class Nave:
    def __init__(self, vida, naveX, naveY, Xcambio, Ycambio):
        self.vida = vida
        self.posX = naveX
        self.posY = naveY
        self.Xcambio = Xcambio
        self.Ycambio = Ycambio

    def get_vida(self):
        return self.vida
    def get_posX(self):
        return self.posX
    def get_posY(self):
        return self.posY
    def get_Xcambio(self):
        return self.Xcambio
    def get_Ycambio(self):
        return self.Ycambio
jugador = Nave(60, 465, 465, 0, 0)

#función del jugador
def jugador(x,y):
    screen.blit(jugadorImg,(get_posX(jugador), get_posY(jugador)))  #blit es la función que "dibuja" al jugador en la pantalla
"""
jugadorX = jugador.X
jugadorY = jugador.Y
jugadorX_cambio = jugador.Xcambio
jugadorY_cambio = jugador.Ycambio
"""

#Proyectil(s)
proyectilImg = pygame.image.load("test_asteroid.png")
proyectilX = random.randint(0,929)
proyectilY = random.randint(0,399)
proyectilX_cambio = random.randint(-15, 15)
proyectilY_cambio = random.randint(-15, 15)

#función de los asteroides
def proyectil(x,y):
    screen.blit(proyectilImg,(x,y))

#función que detecta colisónes
def icolision(x1, y1 , x2, y2):
    distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distancia < 60:
        return True
    else:
        return False

#loop del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                jugador.Ycambio = -5.8
            if evento.key == pygame.K_DOWN:
                jugador.Ycambio = 5.8
            if evento.key == pygame.K_RIGHT:
                jugador.Xcambio = 5.8
            if evento.key == pygame.K_LEFT:
                jugador.Xcambio = -5.8
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador.Xcambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugador.Ycambio = 0

    screen.fill((150,150,150))   #Color de fondo
    screen.blit(fondo, (0,0))

    proyectilX += proyectilX_cambio
    proyectilY += proyectilY_cambio
    if proyectilX <= -10:
        proyectilX_cambio = -proyectilX_cambio
    if proyectilX >= 930:
        proyectilX_cambio = -proyectilX_cambio
    if proyectilY <= -10:
        proyectilY_cambio = -proyectilY_cambio
    if proyectilY >= 600:
        proyectilY_cambio = -proyectilY_cambio

    proyectil(proyectilX, proyectilY)

    jugador.posX += jugador.Xcambio #ju
    jugador.posY += jugador.Ycambio
    if jugador.posX <= 0:
        jugador.posX = 0
    elif jugador.posX >= 900:
        jugador.posX = 900
    elif jugador.posY <= 10:
        jugador.posY = 10
    elif jugador.posY >= 570:
        jugador.posY = 570

    colision = icolision(jugador.posX, jugador.posY, proyectilX, proyectilY)
    if colision:
        jugador.vida -= 1
        print(jugador.vida)
        proyectilX = random.randint(0, 950)
        proyectilY = random.randint(0, 399)
        proyectilX_cambio = random.randint(-15, 15)
        proyectilY_cambio = random.randint(-15, 15)

    jugador(jugador.posX,jugador.posY)

    pygame.display.update()