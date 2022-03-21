''' Bolinha para pontuação do jogo '''

from turtle import Turtle
import random

class Bolinha(Turtle):
    ''' Class para bolinha do jogo '''

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('blue')
        self.speed('fastest')
        self.atualizar()

    def atualizar(self):
        ''' Local aleatorio da bolinha '''
        x_aleatorio = random.randint(-280, 280)
        y_aleatorio = random.randint(-280, 280)
        self.goto(x=x_aleatorio, y=y_aleatorio)
