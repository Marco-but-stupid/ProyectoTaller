import pygame
import random

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

#Asteroide(s)
asteroideImg = pygame.image.load("test_asteroid.png")
asteroideX = random.randint(0,950)
asteroideY = random.randint(0,399)
asteroideX_cambio = random.randint(-8, 8)
asteroideY_cambio = random.randint(-8, 8)

#función del jugador
def jugador(x,y):
    screen.blit(jugadorImg,(x,y))  #blit es la función que "dibuja" al jugador en la pantalla

#función de los asteroides
def asteroide(x,y):
    screen.blit(asteroideImg,(x,y))

#función que detecta colisónes
def colision(jugadorX, jugadorY, asteroideX, asteroideY):

#se crea el loop del juego
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

    asteroideX += asteroideX_cambio
    asteroideY += asteroideY_cambio
    if asteroideX <= -10:
        asteroideX_cambio = -asteroideX_cambio
    if asteroideX >= 930:
        asteroideX_cambio = -asteroideX_cambio
    if asteroideY <= -10:
        asteroideY_cambio = -asteroideY_cambio
    if asteroideY >= 600:
        asteroideY_cambio = -asteroideY_cambio

    asteroide(asteroideX, asteroideY)

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

    jugador(jugadorX,jugadorY)

    pygame.display.update()