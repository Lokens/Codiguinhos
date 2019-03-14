# -- coding: utf-8 --
#Importa o PyGame
import pygame
import time

#Inicia o PyGame
pygame.init()

display_width = 512
display_height = 143

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 62
#Define a janela
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Título da Janela
pygame.display.set_caption('Tutorial UFFS')

#FPS
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
#Carrega a img do carro
carImg = pygame.image.load('car.png')
bgImg = pygame.image.load('bg.png').convert()
enemyImg = pygame.image.load('enemy.png').convert()

def car(carx,cary):
    #Desenha o carro
    gameDisplay.blit(carImg,(carx,cary))

def enemy(ex,ey):
    #Desenha o inimigo
    gameDisplay.blit(enemyImg,(ex,ey))

def bg(x,y):
    #Desenha o fundo
    gameDisplay.blit(bgImg,(0,0))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('BOLUDO')

def game_loop():

    carx = (display_width * 0.45)
    cary = (display_height * 0.8)

    ex = (display_width * 0.15)
    ey = (display_height * 0.8)

    x_change = 0
    y_change = 0

    gameExit = False

    #Enquanto não bater
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Se a tecla for pressionada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            else:
                x_change = 0
                y_change = 0

            #Se a tecla for solta
            #f event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        x_change = 0

        carx += x_change
        cary += y_change

        #Desenha o fundo
        gameDisplay.fill(white)

        #Desenha o carro
        bg(carx,cary)
        car(carx,cary)
        enemy(ex,ey)

        # Detecta se o carro saiu da tela
        if carx > display_width - car_width or carx < 0:
            x_change = 0
            #crash()

        if carx - car_width <= ex:
            crash()
        #Atualiza uma parte da tela
        pygame.display.update()
        clock.tick(20)

game_loop()