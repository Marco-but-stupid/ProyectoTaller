
import pygame

#se inicializa pygame
pygame.init()

#se crea la pantalla
MenuScreen = pygame.display.set_mode((1200, 650))

#Título e ícono
pygame.display.set_caption("Battle At Phobos")
ícono = pygame.image.load(r"C:\Users\josec\Downloads\Proyecto\Marte.png")
pygame.display.set_icon(ícono)


#Se crea la función de loop del menu
Toque = False

def Menu():
    corriendo = True
    while corriendo:

        # Fondo del menu
        FondoMenu = pygame.image.load("PhobosBG.png")
        MenuScreen.blit(FondoMenu, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        Título = font.render("Mars Approach", True, (255, 255, 255))
        TítuloRect = Título.get_rect()
        TítuloRect.center = (1280 // 2, 720 // 2)

        MouseX, MouseY = pygame.mouse.get_pos()

        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)

        if button1.collidepoint((MouseX, MouseY)):
            if Toque:
                about()
        if button2.collidepoint((MouseX, MouseY)):
            if Toque:
                pass

        pygame.draw.rect(MenuScreen, (255, 0, 0), button1)
        pygame.draw.rect(MenuScreen, (255, 0, 0), button2)

        Toque = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    Toque = True
        pygame.display.update()

def about():
    corriendo = True
    while corriendo:
        MenuScreen.fill((0,0,0))
        font2 = pygame.font.Font('freesansbold.ttf', 32)
        #Datos del autor

        #Universidad
        Universidad = font2.render("Instituto Tecnológico de Costa Rica", True, (255, 255, 255))
        UniversidadRect = Universidad.get_rect()
        UniversidadRect.center = (1200 // 2, 32)
        MenuScreen.blit(Universidad, UniversidadRect)

        # Carrera
        Carrera = font2.render("Ingeniería en Computadores", True, (255, 255, 255))
        CarreraRect = Carrera.get_rect()
        CarreraRect.center = (1200 // 2, 106)
        MenuScreen.blit(Carrera, CarreraRect)

        # Asignatura
        Asignatura = font2.render("Taller de Programación", True, (255, 255, 255))
        AsignaturaRect = Asignatura.get_rect()
        AsignaturaRect.center = (1200 // 2, 170)
        MenuScreen.blit(Asignatura, AsignaturaRect)

        # Grupo
        Grupo = font2.render("Grupo 01", True, (255, 255, 255))
        GrupoRect = Grupo.get_rect()
        GrupoRect.center = (1200 // 2, 234)
        MenuScreen.blit(Grupo, GrupoRect)

        # Profesor
        Profesor = font2.render("Jeff Schmidt Peralta", True, (255, 255, 255))
        ProfesorRect = Profesor.get_rect()
        ProfesorRect.center = (1200 // 2, 298)
        MenuScreen.blit(Profesor, ProfesorRect)

        # Autores
        Autores = font2.render("Allan Zheng Tang", True, (255, 255, 255))
        AutoresRect = Autores.get_rect()
        AutoresRect.center = (1200 // 2, 362)
        MenuScreen.blit(Autores, AutoresRect)

        Autores2 = font2.render("Marco Andrés Villatoro Chacón", True, (255, 255, 255))
        Autores2Rect = Autores2.get_rect()
        Autores2Rect.center = (1200 // 2, 426)
        MenuScreen.blit(Autores2, Autores2Rect)

        # Año
        Año = font2.render("2021", True, (255, 255, 255))
        AñoRect = Año.get_rect()
        AñoRect.center = (1200 // 2, 490)
        MenuScreen.blit(Año, AñoRect)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pygame.display.update()

Menu()














