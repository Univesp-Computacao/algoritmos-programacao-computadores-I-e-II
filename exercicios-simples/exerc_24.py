#  Inverter a ordem dos dígitos de um número inteiro.


n1 = int(input("Digite um inteiro: "))
n2 =0

while n1>0:
    digito = n1 % 10
    n1 = n1 // 10
    n2 = n2 *10
    n2 = n2 + digito

print("Número invertido: ", n2)