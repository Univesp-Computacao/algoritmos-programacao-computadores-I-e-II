""""
Considere o seguinte trecho de código:

[código]


O programa irá imprimir:
"""

soma = 0

for i in range(1, 10):

    if i % 2 == 0:  # se par
        soma += i

    else:  # se ímpar
        soma -= i


print(soma)
