# Fatorial (recursão).

def factorial(a):
    if a == 1:
        return a
    return a * factorial(a-1)

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é: {factorial(n)}")