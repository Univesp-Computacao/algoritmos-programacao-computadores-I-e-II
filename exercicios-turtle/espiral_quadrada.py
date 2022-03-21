from turtle import Screen, Turtle

tela = Screen()
tela.setup(800, 700, startx=0, starty=100)
tartaruga = Turtle()
tartaruga.speed(20)

for x in range(0, 500, 1):
    tartaruga.forward(x)
    tartaruga.left(91)
