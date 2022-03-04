# Programa que calcula o fatorial de um inteiro

numero = int(input("Digite um número:"))

# esse número recebido deverá a cada iteração se multiplicar,
# em seguida subtrair uma unidade, tornar a se multiplicar,
# até que reste o número um, que desfaz o laço e dá o resultado

factorial = 1
while numero > 1:
    factorial *= numero
    numero -= 1
print(factorial)
