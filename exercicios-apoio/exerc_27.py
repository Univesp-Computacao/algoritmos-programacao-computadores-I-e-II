"""
Implemente um programa que solicite do usuário uma lista de palavras
(ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de
quatro letras nessa lista.
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare pote
"""

def exerc_27(lista):
    return list(filter(lambda x: len(x) == 4, lista))

print(exerc_27(['pare', 'desktop', 'tio', 'pote']))
