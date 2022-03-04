# Inverter a ordem dos dígitos de um número inteiro.
# usando operações aritméticas

n1 = int(input("Digite um inteiro: "))
# novo número
n2 = 0

while n1 > 0:
    # último dígito
    digito = n1 % 10
    # deleta o último dígito do número inserido
    n1 = n1 // 10
    # aumenta
    n2 = n2 * 10
    # adiciona o dígito
    n2 = n2 + digito

print("Número invertido: ", n2)
