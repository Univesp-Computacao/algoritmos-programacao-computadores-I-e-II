"""
Primeiro, execute a atribuição palavras =
['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a
primeira e a última palavras em palavras, na ordem do dicionário.
"""

def exerc_2(*args):
    "Organizador de listas."
    print(sorted(*args))
    return sorted(*args)

exerc_2(['taco', 'bola', 'celeiro', 'cesta', 'peteca']) # Output => ['bola', 'celeiro', 'cesta', 'peteca', 'taco']