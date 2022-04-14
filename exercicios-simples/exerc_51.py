# Checar se três número são primos.

from math import sqrt

def validarPrimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True
for i in range(3):
    num = int(input("Digite o número que quer validar"))
    print(validarPrimo(num))