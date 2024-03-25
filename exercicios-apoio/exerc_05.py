"""
Escreva expressões algébricas Python correspondentes aos seguintes comandos:  
a) A soma dos 5 primeiros inteiros positivos.
b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
c) O número de vezes que 73 cabe em 403.
d) O resto de quando 403 é dividido por 73.
e) 2 à 10ª potência.
f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
"""

# a)
print("A soma dos 5 primeiros inteiros positivos é",sum([1,2,3,4,5])) 
    # Output => 15

# b)
def exerc_05_b(*args):
    print('(float) A idade média deles é', sum(args) / len(args))
    print('(int) A idade média deles é', sum(args) // len(args)) 
exerc_05_b(23,19,31)
    # Output => 24.333333333333332
    # Output => 24

# c)
print("(float) O número de vezes que 73 cabe em 403", 403 / 73)
print("(int) O número de vezes que 73 cabe em 403", 403 // 73) 
    # Output => 5.52054794520548
    # Output => 5

# d)
print("O resto de quando 403 é dividido por 73.", 403 % 73) 
    # Output => 38


# e)
print("2 à 10ª potência.", 2**10) 
    # Output => 1024

# f)
print("O valor absoluto da distância entre as alturas",abs(54 - 57)) 
    # Output => 3

# g)
print("O menor preço entre os preços é", min([34.99, 29.95, 31.50]))
    # Output => 29.95