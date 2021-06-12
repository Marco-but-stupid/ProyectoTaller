import pygame

#se inicializa pygame
pygame.init()

#se crea la pantalla
screen = pygame.display.set_mode((1200, 650))

#Título e ícono
pygame.display.set_caption("Mars approach")
ícono = pygame.image.load("Marte.png")
pygame.display.set_icon(ícono)

#Jugador
jugadorImg = pygame.image.load("Arcadia.png")
jugadorX = 465
jugadorY = 465
jugadorX_cambio = 0
jugadorY_cambio = 0

#función del jugador
def jugador(x,y):
    screen.blit(jugadorImg,(x,y))  #blit es la función que "dibuja" al jugador en la pantalla

#se crea el loop del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                jugadorY_cambio = -1.5
            if evento.key == pygame.K_DOWN:
                jugadorY_cambio = 1.5
            if evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 1.5
            if evento.key == pygame.K_LEFT:
                jugadorX_cambio = -1.5
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugadorY_cambio = 0

    screen.fill((150,150,150))   #Color de fondo

    jugadorX += jugadorX_cambio

    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 1100:
        jugadorX = 1100
    elif jugadorY <= 10:
        jugadorY = 10
    elif jugadorY >= 540:
        jugadorY = 540

    jugadorY += jugadorY_cambio

    jugador(jugadorX,jugadorY)

    pygame.display.update()