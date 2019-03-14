import pygame
from random import *
#cores
verde=(0,205,0)
Verde_escuro=(0,100,0)
cinza=(66,66,66)


pygame.init()

#tamanho da tela
#tela do pygame é um plao cartesiano
altura=480
largura=640
fundo=pygame.display.set_mode((largura,altura))

#tamanho e posição
tamanho=10
pos_x=randint(0,(largura-tamanho)/10)*10
pos_y=randint(0,(altura-tamanho)/10)*10

#velociade do objeto
velocidade_x=0
velocidade_y=0

#nome do jogo
pygame.display.set_caption('SNAKE')

#loop do jogo
sair = True

while sair :
    #fechar o game no X
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            sair = False
        #setar os controles de movimento
        if event.type == pygame.KEYDOWN:

                # seta esquerda move
                if event.key == pygame.K_LEFT :
                    velocidade_y = 0
                    velocidade_x = -0.5

                #vove pra direita
                if event.key == pygame.K_RIGHT :
                    velocidade_y=0
                    velocidade_x=+0.5

                    #move pra cima
                if event.key == pygame.K_UP :
                    velocidade_y =- 0.5
                    velocidade_x = 0

                #move pra baixo
                if event.key == pygame.K_DOWN:
                    velocidade_y =+ 0.5
                    velocidade_x = 0



    #preenche o fundo com a cor
    fundo.fill(verde)

    #objeto jogavel
    pygame.draw.rect(fundo,cinza,[pos_x,pos_y,tamanho,tamanho])

    #pra continuar sempre andando
    pos_x+=velocidade_x
    pos_y+=velocidade_y

    #atualizar tela sempre no loop
    pygame.display.update()



