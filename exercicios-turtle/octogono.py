import turtle
import time

ws = turtle.Screen()

t = turtle.Turtle()

t.pencolor("blue")
t.speed(3)
t.pensize(5)

# o loop abaixo será executado 08 vezes
# a cada iteração a caneta andará 100 e depois girará 45º à esquerda
for i in range(8):
    t.forward(100)
    t.left(45)

time.sleep(2)