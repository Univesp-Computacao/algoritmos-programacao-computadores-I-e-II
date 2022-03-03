# Preencher uma array com números randômicos.

from random import randint

n = 10
array = []

for i in range(n):
    array.append(randint(1,99))

print(array)