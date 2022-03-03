# Factorial

numero = int(input("Digite um número:"))

factorial = 1
while numero > 1:
    factorial *= numero
    numero -= 1
print(factorial)
