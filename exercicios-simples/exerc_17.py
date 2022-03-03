# Adivinhar o número randômico

from random import randint

numero_secreto = randint(1,100)

numero_usuario = -1

contagem_tentativas = 1

while numero_secreto != numero_usuario:
    print(f"Tentativa: {contagem_tentativas}")
    numero_usuario = int(input("Digite sua tentativa"))
    if numero_usuario < numero_secreto:
        print("O número secreto é maior")
    elif numero_usuario > numero_secreto:
        print("O número secreto é menor")
    else:
        print("você adivinhou")
    contagem_tentativas +=1