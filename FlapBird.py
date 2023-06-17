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


class cano:
    pass

class chao:
    pass