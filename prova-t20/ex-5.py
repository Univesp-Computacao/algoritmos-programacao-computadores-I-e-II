""""
Questão dissertativa

A média harmônica é definida como :

[definição de média harmônica]

onde N é o número de notas a serem usadas na média, nié a i-ésimanota,
e X é o fator de amortização. Implemente uma função em Python que calcule
a média de 3 notas de um aluno digitadas no teclado, com fator de amortização
igual a 4. Em seguida, informe se o aluno passou (média >= 5) ou não (média < 5).
"""


def calcula_media(n1, n2, n3):
    media = (3 / (
            (1 / (n1 + 4)) +
            (1 / (n2 + 4)) +
            (1 / (n3 + 4)))) - 4
    return media


n1 = eval(input('Digite a nota 1: '))
n2 = eval(input('Digite a nota 2: '))
n3 = eval(input('Digite a nota 3: '))

media = calcula_media(n1, n2, n3)

if media >= 5:
    print('Você passou, sua média é ', media)
else:
    print('Você não passou, sua média é ', media)
