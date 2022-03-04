# Deletar um item randômico de um dicionários.

import random

dicionario = {"A": 4, "O": 6, "P": 10, "M": 7, "B": 3}

print(dicionario)

# o método keys() cria um objeto contendo as chaves do dicionário
chaves = list(dicionario.keys())
# o método choice() seleciona aleatoriament um número de uma sequência.
qual_deletar = random.choice(chaves)
# removendo o item
del dicionario[qual_deletar]
print(dicionario)
