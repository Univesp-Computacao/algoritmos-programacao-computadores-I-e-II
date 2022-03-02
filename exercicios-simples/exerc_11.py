# Checando a divisibilidade de um inteiro por outro.

numero_1 = int(input("Digite o dividendo"))
numero_2 = int(input("Digite o divisor"))

# verificando o resto com muodulus operator
if numero_1 % numero_2 == 0:
    print(" É divisível")
else:
    print(f"não é divisível, o resto é {numero_1 % numero_2}")