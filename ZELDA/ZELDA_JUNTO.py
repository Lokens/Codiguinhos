import pygame,sys
from pygame.locals import *
import random

# Tamanho da tela
largura=1280
altura=720

class orc (pygame.sprite.Sprite) :
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
       #imagne sdo inimigo
        self.imagem_orc1 = pygame.image.load('inimigo.png')
        self.imagem_orc2 = pygame.image.load('orc2.png')

        #lista para borar varios inimigos
        self.lista_imagens = [self.imagem_orc1 , self.imagem_orc2]
        self.pos_imagem = 0
        self.imagem_inimigo = self.lista_imagens [self.pos_imagem]


        self.rect = self.imagem_inimigo.get_rect()

        self.listadisparo = []
        self.velocidade  = 10
        self.rect.top = posy
        self.rect.left = posx

        #tempo de spawn dos inimigos
        self.spawn_inimigo = 10


    #trajetoria da espada
    def comportamento (self,tempo) :
        if self.spawn_inimigo == tempo :
            self.pos_imagem += 1
            self.spawn_inimigo += 1
            if self.pos_imagem > len(self.lista_imagens)-1 :
                self.pos_imagem = 0



    #para colocar espada na tela
    def colocar (self, superficie) :
        self.imagem_inimigo = self.lista_imagens[self.pos_imagem]
        superficie.blit(self.imagem_inimigo, self.rect)


class espada (pygame.sprite.Sprite) :
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_espada = pygame.image.load('espada.png')

        self.rect = self.imagem_espada.get_rect()
        self.velocidade_espada = 5
        self.rect.top = posy
        self.rect.left = posx

    #trajetoria da espada
    def trajetoria (self) :
        self.rect.top = self.rect.top - self.velocidade_espada

    #para colocar espada na tela
    def colocar (self, superficie) :
        superficie.blit(self.imagem_espada, self.rect)



#criando o player
class link (pygame.sprite.Sprite) :
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global imagem_link
        imagem_link = ['cima.png', 'baixo.png', 'esq.png', 'dir.png']
        self.imagem_link = pygame.image.load(imagem_link[0])

        #criando a hitbox
        self.rect = self.imagem_link.get_rect()

        #posição do jogador
        self.rect.centerx = largura/2
        self.rect.centery = altura - 100


        #Adicionais do jogo
        self.listaDisparo = []
        self.vida = True
        self.velocidade = 10



    def movimento (self):
        if self.vida == True :

            #não sair a esquerda
            if self.rect.left <= -15 :
              self.rect.left = -5

            #não sair a direita
            elif self.rect.right >= largura :
                self.rect.right = largura


            # não sair para cima
            elif self.rect.top >= 530:
                self.rect.top = 530

            # # não sair a baixo
            elif self.rect.bottom <= 120:
                 self.rect.bottom = 120


    def atacar (self, x, y):
        minha_espada= espada (x - 22 ,y - 73 )
        self.listaDisparo.append(minha_espada)


    #para colocar algo na tela
    def colocar(self, superficie) :
        superficie.blit(self.imagem_link,self.rect)


    ###QUANDO QUISER BOTAR QUALQUER COMANDO OU AÇÃO FAZER UMA DEF AQUI


#começa o game
def zelda ():
    pygame.init()
    tela = pygame.display.set_mode((largura,altura))
    #,pygame.FULLSCREEN)
    pygame.display.set_caption('ZELDA ARENA')


    jogador = link()
    imagem_fundo = pygame.image.load('arena.png')

    #para mudar se algo o fizer parar de jogar
    jogando=True


    inimigo = orc (100 ,100 )


    #daonde sai a espada
    espada_link = espada (largura / 100 , altura - 150)

#FPS
    relogio = pygame.time.Clock()



#fecha o game e bota os objetos

    while True :
        #FPS
        relogio.tick(60)

        #relogio do jogo
        tempo =int(pygame.time.get_ticks()/1000)

        #pra iniciar a bareira e não passar do lado
        jogador.movimento()

        espada_link.trajetoria()

        #evento q fecha o game
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                #isso ^ é igual a um break
                #break
                # movimentação do personagem
        if evento.type == pygame.KEYDOWN:

            if evento.key == K_LEFT:
                jogador.imagem_link = pygame.image.load(imagem_link[2])
                jogador.rect.left -= jogador.velocidade

            elif evento.key == K_RIGHT:
                jogador.imagem_link = pygame.image.load(imagem_link[3])
                jogador.rect.right += jogador.velocidade

            elif evento.key == K_UP:
                jogador.imagem_link = pygame.image.load(imagem_link[0])
                jogador.rect.top -= jogador.velocidade


            elif evento.key == K_DOWN:
                jogador.imagem_link = pygame.image.load(imagem_link[1])
                jogador.rect.bottom += jogador.velocidade

            else:
                jogador.rect.top += 0


                #ataque
                if evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.atacar (x,y)

            if evento.key == K_ESCAPE :
                pygame.quit()
                sys.exit()

        #colocar os objetos na  tela
        tela.blit(imagem_fundo, (0, 0))
        jogador.colocar(tela)
        inimigo.colocar(tela)
        inimigo.comportamento(tempo)

        if len(jogador.listaDisparo) > 0 :
            for z in jogador.listaDisparo :
                z.colocar(tela)
                z.trajetoria()

                #limitar aonde o tiro vai
                if z.rect.top < 455 :
                    jogador.listaDisparo.remove(z)



        pygame.display.update()



zelda()