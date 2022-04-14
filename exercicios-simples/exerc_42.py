# Deletar um item randômico de um dicionário.

import random

# criação manual de um dicionário
dicionario = {"A": 4, "O": 6, "P": 10, "M": 7, "B": 3}

print(dicionario)

# o método keys() cria um objeto contendo as chaves do dicionário
# criamos uma variável "chaves" que armazenará as chaves do dicionário em forma de lista
chaves = list(dicionario.keys())

# o método choice() seleciona aleatoriamente um número de uma sequência.
# criamos uma variável "qual_deletar" que recebe esse item da lista de chaves.
qual_deletar = random.choice(chaves)

# removendo o item com del
del dicionario[qual_deletar]
print(" \n O novo dicionário é: \n",dicionario, "\n E o valor removido foi o:", qual_deletar)
