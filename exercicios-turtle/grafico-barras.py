# Python program to draw a turtle
import turtle


# Function that draws the turtle
def desenha_barras(t, height, color):
    # Começa o preenchimento
    t.fillcolor(color)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)

    # para o preenchimento
    t.end_fill()


# xs é uma lista que recebe número de barras e suas alturas

xs = [48, 117, 150, 96, 134, 160, 90]
clrs = ["green", "red", "yellow", "black",
        "pink", "brown", "blue"]

maxheight = max(xs)
numbars = len(xs)
border = 7

# Set up the window and its
# attributes
wn = turtle.Screen()
wn.setworldcoordinates(0 - border, 0 - border,
                       80 * numbars + border,
                       maxheight + border)

# Cria instância da classe
tess = turtle.Turtle()
tess.pensize(3)

for i in range(len(xs)):
    desenha_barras(tess, xs[i],
                   clrs[i])

wn.exitonclick()
