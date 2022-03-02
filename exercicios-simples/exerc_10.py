#  Determinar o maior inteiro de três.

numero_1 = int(input("Digite o primeiro número"))
numero_2 = int(input("Digite o segundo número"))
numero_3 = int(input("Digite o terceiro número"))

print(" o maior número dos três é: \n")
if numero_2 <= numero_1 >= numero_3:
    print(numero_1)
elif numero_1 <= numero_2 >= numero_3:
    print(numero_2)
else:
    print(numero_3)