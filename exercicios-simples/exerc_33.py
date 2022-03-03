# Selection sort
from random import randint

n = 7
a = []
for i in range(n):
    a.append(randint(1,20))
print(a)

j = n - 1
while j >0:
    ind = 0
    for i in range (1, j+1):
        if a[i] > a[ind]:
            ind = i
    b = a[ind]
    a[ind] = a[j]
    a[j] = b
    j -= 1
print(a)