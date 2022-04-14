import time
import datetime as dt
import turtle

# cria duas instâncias do objeto turtle
t = turtle.Turtle()  # para a hora em si
t1 = turtle.Turtle()  # para a borda

# cria a tela (SCREEN)
s = turtle.Screen()

# escolhe a cor de fundo da tela
s.bgcolor("green")

# cria três variáveis que armazenam a hora atual
segundos = dt.datetime.now().second
minutos = dt.datetime.now().minute
hora = dt.datetime.now().hour

# define a grossura (width) e a cor da caneta da borda para a instância t1
t1.pensize(3)
t1.color('black')

t1.penup()
t1.goto(-20, 0)
t1.pendown()

# desenha a borda
for i in range(2):
    t1.forward(200)  # distância horizontal
    t1.left(90)  # graus para a esquerda
    t1.forward(70)  # distância vertical
    t1.left(90)  # retorna para direita

# esconde a tartaruga t1
t1.hideturtle()

# cria um loop infinito que mantém a hora atualizada
while True:
    # mantém escondida a tartaruga t
    t.hideturtle()
    t.clear()

    # usa o método write() passando as horas, minutos e segundo
    # usa-se o zfill() para que sempre tenham duas casas, p.ex. quando for "2 horas" mostrará "02 horas"
    # e define o parâmetro font=()
    t.write(str(hora).zfill(2)
            + ":" + str(minutos).zfill(2) + ":"
            + str(segundos).zfill(2),
            font=("Arial Narrow", 35, "bold"))

    # pausa o programa por 01 segundo
    time.sleep(1)

    # aumenta manualmente os segundos
    segundos += 1

    # lógica de um relógio digital
    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        hora += 1

    if hora == 24:
        hora = 1
