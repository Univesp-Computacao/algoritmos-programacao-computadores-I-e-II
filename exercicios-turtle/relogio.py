
import turtle
import time
screen = turtle.Screen()
# configuração da tela
screen.setup(500, 500)
# instância turtle
clk = turtle.Turtle()
# cor da tartaruga
clk.color('Green')
# espessura contorno
clk.width(4)
def draw_hour_hand():
    clk.penup()
    clk.home()
    clk.right(90)
    clk.pendown()
    clk.forward(100)
# valores numericos do relogio
val = 0
# loop para imprimir numeros
for i in range(12):
    # incrementa 1
    val += 1
    # move a tartaruga
    clk.penup()
    # movimento circular
    clk.setheading(-30 * (i + 3) + 75)

    clk.forward(22)
    # coloca caneta na superfície
    clk.pendown()
    # move para linha tracejada
    clk.forward(15)

    clk.penup()

    clk.forward(20)
    # escreve numeros
    clk.write(str(val), align="center",
              font=("Arial",
                    12, "normal"))

clk.setpos(2, -112)
clk.pendown()
clk.width(2)
# preencher de verde
clk.fillcolor('Green')
# começa preenchimento
clk.begin_fill()
# faz circulo de radius 5
clk.circle(5)
# fim preenchimento
clk.end_fill()
clk.penup()
draw_hour_hand()
clk.setpos(-20, -64)
clk.pendown()
clk.penup()
# seleciona posição e escreve texto
clk.setpos(-30, -170)
clk.pendown()
clk.write(' Relógio com \n Turtle', font=("Arial", 12,
                              "normal"))
clk.hideturtle()
turtle.done()
time.sleep(2)