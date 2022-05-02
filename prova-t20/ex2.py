""""
Dada uma lista definida como:

lista = [[1], [[2, 3], 4], 5, [], [6, 7], [[8]], [9, 10]]

Assinale a alternativa que corresponde ao comando que irá retornar o número 1:
"""

lista = [
    [1],  # 0
    [[2, 3], 4],  # 1
    5,  # 2
    [],  # 3
    [6, 7],  # 4
    [[8]], # 5
    [9, 10] # 6
]

print(lista[0])
print(lista[0][0])

print(lista[4][1])
