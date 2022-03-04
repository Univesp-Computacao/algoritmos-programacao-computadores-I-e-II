# O número é par ou ímpar?

# Recebe a entrada de um numero inteiro
numero = int(input("Digite um número"))

# Condição usando o modulus operator, que retorna o resto de uma divisão.
# Se o resto da divião por dois é zero então é par, senão, é ímpar.
if numero % 2 == 0:
    print("par")
else:
    print("ímpar")
