import pygame  # bliblioteca de jogos
import random  # geração de numeros aleatorios
import os      # integra os codigos com os arquivos do computador

from pygame.font import Font

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))

IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))

IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()

FONTE_PONTOS: Font = pygame.font.SysFont('arial', 50)


class passaro:
    IMGS = IMAGENS_PASSARO

    # ANIMAÇÕES DA ROTAÇÃO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    # ATRIBUTOS DO PASSARO

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0  #quando o passaro se movimentar, será definido em quanto tempo ele vai demorar pra voltar ao movimento inicial após pular
        self.imagem = IMGS[0]  # saber qual imagem do passaro esta sendo usada, a primeira, segunda ou terceira

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo


    #Restringir o deslocamento
        if deslocamento > 16:
            deslocamento == 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

    #Angulo do passaro

        if deslocamento < 0 or self.y < self.altura + 50: #quando o bendito do passaro voltar ao eixo inicial dele, ele vai virar o bico pra baixo pra animação de queda
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        elif self.angulo > -90:
                self.angulo <= self.VELOCIDADE_ROTACAO

class cano:
    pass

class chao:
    pass