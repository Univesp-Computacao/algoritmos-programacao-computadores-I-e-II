# Sequência de Fibonacci.

# entrada
numero_elemtos = int(input("Digite o número de elementos"))

# associação múltipla
f1 = f2 = 1

# os dois primeiros são 1
print (f1, f2, end=' ')

i = 2
# Lógica da adição
while i < numero_elemtos:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    i += 1

print()