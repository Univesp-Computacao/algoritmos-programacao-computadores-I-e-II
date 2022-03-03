# Sequência de Fibonacci.

def fibNumero(item):
    f1 = f2 = 1
    while item>2:
        buffer = f2
        f2 = f1 + f2
        f1 = buffer
        item -=1
    return f2

def fibSequencia(item):
    f1 = f2 = 1
    print(f1,f2,end=' ')
    while item > 2 :
        buffer = f2
        f2 = f1+ f2
        f1 = buffer
        print(f2,end=' ')
        item -= 1
    print()

n = int(input("Digite um número"))

m = fibNumero(n)

print(m)

fibSequencia(n)