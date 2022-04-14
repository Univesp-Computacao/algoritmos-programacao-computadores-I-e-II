import turtle
import time

sc = turtle.Screen()

pen = turtle.Turtle()


def semi_circle(col, rad, val):
    # atribui cor à caneta
    pen.color(col)

    # desenha um semicirculo com o método circle()
    # no caso, -180 é um parâmetro opcional, por default circle() desenha um circulo completo.
    pen.circle(rad, -180)

    # levanta a caneta, ou seja, NÃO desenha enquanto se move
    pen.up()

    # reposiciona a caneta
    pen.setpos(val, 0)

    # abaixa a caneta e reposiciona o ângulo
    pen.down()
    pen.right(180)


col = ['violet', 'indigo', 'blue',
       'green', 'yellow', 'orange', 'red']

# tamanho da tela
sc.setup(600, 600)

# cor de fundo
sc.bgcolor('#d6ffff')

pen.right(90)  # angulo a direita
pen.width(10)  # espessura do contorno
pen.speed(7)  # velocidade do desenho

# cria um laço iterativo que irá ser executadoi 07 vezes
# para cada iteração será selecionado uma cor diferente e
# a caneta será reposicionada
for i in range(7):
    semi_circle(col[i], 10 * (
            i + 8), -10 * (i + 1))

time.sleep(1)

pen.hideturtle()
