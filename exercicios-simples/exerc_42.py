# Deletar um item randômico de um dicionários.

import random

dicionario = {"A": 4, "O": 6, "P": 10, "M": 7, "B": 3}

print(dicionario)

chaves = list(dicionario.keys())
qual_deletar = random.choice(chaves)
del dicionario[qual_deletar]
print(dicionario)
