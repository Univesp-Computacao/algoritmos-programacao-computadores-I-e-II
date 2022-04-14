# import for turtle
import turtle
import time

# tela de trabalho (working screen)
ws = turtle.Screen()

# inicia instância turtle
t = turtle.Turtle()
t.pensize(5)

# executa o loop por 05 vezes
for i in range(5):

		# movendo 120 unidades para frente
		t.forward(120)

		# rotacionando a tartaruga 144º a direita
		t.right(144)
time.sleep(2)