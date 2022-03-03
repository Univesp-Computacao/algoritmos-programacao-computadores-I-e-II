# Separar positivos e negativos de uma array.

from random import random

a = []
for i in range(7):
    n = int(random() * 20) - 10
    a.append(n)

print(a)
neg = []
pos = []
for i in a:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)
print("Negativos: ",neg)
print("Positivos: ",pos)