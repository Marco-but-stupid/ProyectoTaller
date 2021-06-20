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
jugadorX = 465
jugadorY = 465
jugadorX_cambio = 0
jugadorY_cambio = 0
jugador_vida = 20

#Proyectil(s)
proyectilImg = pygame.image.load("test_asteroid.png")
proyectilX = random.randint(0,929)
proyectilY = random.randint(0,399)
proyectilX_cambio = random.randint(-15, 15)
proyectilY_cambio = random.randint(-15, 15)


#función del jugador
def jugador(x,y):
    screen.blit(jugadorImg,(x,y))  #blit es la función que "dibuja" al jugador en la pantalla

#función de los asteroides
def proyectil(x,y):
    screen.blit(proyectilImg,(x,y))

#función que detecta colisónes
def icolision(jugadorX, jugadorY, proyectilX, proyectilY):
    distancia = math.sqrt(math.pow(proyectilX - jugadorX, 2) + math.pow(proyectilY - jugadorY, 2))
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
                jugadorY_cambio = -5.8
            if evento.key == pygame.K_DOWN:
                jugadorY_cambio = 5.8
            if evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 5.8
            if evento.key == pygame.K_LEFT:
                jugadorX_cambio = -5.8
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugadorY_cambio = 0

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

    jugadorX += jugadorX_cambio
    jugadorY += jugadorY_cambio
    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 900:
        jugadorX = 900
    elif jugadorY <= 10:
        jugadorY = 10
    elif jugadorY >= 570:
        jugadorY = 570

    colision = icolision(jugadorX, jugadorY, proyectilX, proyectilY)
    if colision:
        jugador_vida -= 1
        print(jugador_vida)
        proyectilX = random.randint(0, 950)
        proyectilY = random.randint(0, 399)
        proyectilX_cambio = random.randint(-15, 15)
        proyectilY_cambio = random.randint(-15, 15)

    jugador(jugadorX,jugadorY)

    pygame.display.update()