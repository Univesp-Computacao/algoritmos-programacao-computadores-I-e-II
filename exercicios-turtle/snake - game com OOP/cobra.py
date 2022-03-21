''' Usando a orientação a objetos, crie uma classe que represente uma cobra.'''

from turtle import Turtle

posição_inicial_x = [(0, 0), (0,-20), (0,-40)]
andar_para_frente = 20
alto = 90
baixo = 270
esquerda = 180
direita = 0

class Cobra:
    ''' Classe da cobrinha do jogo '''

    def __init__(self):
        ''' Inicialização da classe '''
        self.cobra = []
        self.cria_cobrinha()
        self.head = self.cobra[0]

    def cria_cobrinha(self):
        ''' cobrinha do jogo '''
        for posição in posição_inicial_x:
            self.adicionar_parte(posição)


    def adicionar_parte(self, posição):
        ''' adiciona parte da cobra '''
        nova_parte = Turtle("square")
        nova_parte.color("white")
        nova_parte.penup()
        nova_parte.goto(posição)
        self.cobra.append(nova_parte)

    def extender_cobrinha(self):
        ''' Aumenta o tamanho da cobrinha quando ela começa a comer '''
        self.adicionar_parte(self.cobra[-1].position())

    def mover_cobra(self):
        ''' Movimenta a cobrinha automatico'''
        for i in range(len(self.cobra) - 1, 0, -1):
            self.cobra[i].goto(x=self.cobra[i-1].xcor(), y=self.cobra[i-1].ycor())
        self.head.forward(andar_para_frente)

    def mover_para_direita(self):
        ''' Muda a direção para direita sempre no angulo de 90 graus '''
        if self.head.heading() != esquerda:
            self.head.setheading(direita)

    def mover_para_esquerda(self):
        ''' Muda a direção para esquerda sempre no angulo de 90 graus '''
        if self.head.heading() != direita:
            self.head.setheading(esquerda)

    def mover_para_cima(self):
        ''' Muda a direção para cima sempre no angulo de 90 graus '''
        if self.head.heading() != baixo:
            self.head.setheading(alto)


    def mover_para_baixo(self):
        ''' Muda a direção para baixo sempre no angulo de 90 graus '''
        if self.head.heading() != alto:
            self.head.setheading(baixo)

    def resetar_cobrinha(self):
        ''' Reseta a cobrinha quando o jogador perde '''
        for cobrinha in self.cobra:
            cobrinha.goto(1000, 1000)
        self.cobra.clear()
        self.cria_cobrinha()
        self.head = self.cobra[0]
