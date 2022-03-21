''' Exercicio do dia 20 '''

from turtle import Screen
from time import sleep
from cobra import Cobra
from bolinha import Bolinha
from pontuacao import Pontuação

cobra = Cobra()
bolinha = Bolinha()
jogo_esta_online = True
Pontos = Pontuação()

# Objeto da classe Screen
cenario = Screen()
cenario.setup(width=600, height=600)
cenario.bgcolor('black')
cenario.title('Ilha das Cobras')
cenario.tracer(0)
cenario.listen()
cenario.onkey(cobra.mover_para_direita, 'Right')
cenario.onkey(cobra.mover_para_esquerda, 'Left')
cenario.onkey(cobra.mover_para_cima, 'Up')
cenario.onkey(cobra.mover_para_baixo, 'Down')


while jogo_esta_online:
    cenario.update()
    sleep(0.1)
    cobra.mover_cobra()

    # detectar colisão
    if cobra.head.distance(bolinha) < 15:
        bolinha.atualizar()
        Pontos.adicionar_ponto()
        cobra.extender_cobrinha()

    # detectar colisão com a parede
    if cobra.head.xcor() > 285 or cobra.head.xcor() < -285 or cobra.head.ycor() > 285 or cobra.head.ycor() < -285:
        Pontos.resetar()
        cobra.resetar_cobrinha()

    # detectar colisão com a própria cobra
    for parte in cobra.cobra[1:]:
        if cobra.head.distance(parte) < 10:
            Pontos.resetar()
            cobra.resetar_cobrinha()

cenario.exitonclick()
