''' Pontuação do jogo '''

from turtle import Turtle
import os

alinhamento = 'center'
fonte = ('Arial', 20, 'normal')
arquivo = os.path.abspath(r'Nivel - Intermediario dia 15 a 58/dia 23/pontuação.txt')

class Pontuação(Turtle):
    ''' Registrar a pontuação do jogo '''

    def __init__(self):
        ''' Inicializa a classe mãe e registra a pontuação '''
        super().__init__()
        self.pontuação = 0
        self.color('white')
        self.hideturtle()
        with open(arquivo, encoding='UTF-8') as dados:
            self.maior_pontuação = int(dados.read())
        self.penup()
        self.goto(x=0, y=270)
        self.atualizar_pontuacao()

    def atualizar_pontuacao(self):
        ''' Atualizar a informação na pontuação '''
        self.clear()
        self.write(f'Pontuação: {self.pontuação} Maior Pontuação: {self.maior_pontuação}',
                    font=fonte, align=alinhamento)

    def resetar(self):
        ''' Resete e contabilização do jogo '''
        if self.pontuação > self.maior_pontuação:
            self.maior_pontuação = self.pontuação
            with open(arquivo, 'w', encoding='UTF-8') as dados:
                dados.write(str(self.maior_pontuação))
        self.pontuação = 0
        self.atualizar_pontuacao()

    def adicionar_ponto(self):
        ''' Adiciona pontos ao registro de pontuação '''
        self.pontuação += 1
        self.atualizar_pontuacao()
