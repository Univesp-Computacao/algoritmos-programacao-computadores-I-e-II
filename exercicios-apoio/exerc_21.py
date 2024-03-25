# Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.

def Exercicio32c(golpes=int, defesas=int):
    if (golpes > 10 and defesas == 0):
        print("Você está morto")

Exercicio32c(9,1)
Exercicio32c(9,0)
Exercicio32c(10,1)
Exercicio32c(11,0)