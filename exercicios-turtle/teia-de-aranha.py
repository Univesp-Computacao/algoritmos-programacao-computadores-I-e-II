""""


O laço interno se preocupa com a construção de uma única espiral em espiral e com as camadas da teia,
enquanto o laço externo controla o número de espirais a serem construídas.


"""

# importando o módulo turtle como "t", não precisamos instanciar a classe
import turtle as t
import time

t.speed(2)

# A tartaruga é movida para frente e para trás para construir primeiro os fios.
# A tartaruga é girada em um ângulo de 60 graus para desenhar cada fio .
for i in range(6):
    t.forward(100)
    t.backward(100)
    t.right(60)
side = 50  # O comprimento da rosca espiral é definido como 50
t.fillcolor("Yellow")
t.begin_fill()

# O laço interno se preocupa com a construção de uma única espiral em espiral e com as camadas da teia,
# enquanto o laço externo controla o número de espirais a serem construídas.
for i in range(10):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(0)
    t.forward(side)
    t.right(120)

    for j in range(6):
        t.forward(side - 2)
        t.right(60)
    side = side - 10  # reduzimos o tamanho em 10 a cada iteração.

t.end_fill()
time.sleep(2)
