# A soma e o produto dos dígitos de um número.

a = abs(int(input("Digite um inteiro: ")))

soma = 0
mult = 1

while a > 0:
    digito = a % 10
    soma += digito
    mult *= digito
    a = a // 10

print("Soma:", soma)
print("Multiplicação:", mult)
