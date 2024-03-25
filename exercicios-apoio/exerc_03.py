"""
Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética
(variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno
Reprovado com média”. Informar também, após a apresentação das mensagens, o valor
da média obtida pelo aluno.
"""
def exerc_03(nota_minima, *args):
    "Calculadora de média escolar."
    MD = (sum(args)) / len(args)
    if (MD >= nota_minima):
        print("Aluno Aprovado com média", MD)
    else:
        print("Aluno Reprovado com média", MD)

exerc_03(6, 1, 1, 1, 1) # Output => Aluno Reprovado com média 1.0
exerc_03(6, 5, 5, 5, 5) # Output => Aluno Reprovado com média 5.0
exerc_03(6, 10, 10, 10, 10) # Output => Aluno Reprovado com média 10.0
exerc_03(6, 2, 7, 6, 4) # Output => Aluno Reprovado com média 4.75
exerc_03(6, 6, 6, 6, 6) # Output => Aluno Aprovado com média 6.0
