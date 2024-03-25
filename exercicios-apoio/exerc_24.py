import random
"""
Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba
'Melhor sorte da próxima vez…'.
"""

def Exercicio33b(lista=set):
    lista_loteria = random.sample(range(1, 60), 6)
    if (sorted(lista) == sorted(lista_loteria)):
        print('Você ganhou!')
        return True
    else:
        print('Melhor Sorte da Próxima vez')
        return False

Exercicio33b([2,10,7,8,9,14])
