# Sequência de FIbonacci (recursão).

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite um número para descobrir seu valor na sequência: "))
print(fibonacci(num))