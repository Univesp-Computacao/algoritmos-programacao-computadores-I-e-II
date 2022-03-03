# Preencher uma matrix com números randômicos.
from random import randint

n = 5
m = 10
a = []

for i in range(n):
    b = []
    for j in range(m):
        b.append(randint(1, 9))
    a.append(b)
for i in a:
    for j in i:
        print("3%d" % j, end=' ')
    print()
