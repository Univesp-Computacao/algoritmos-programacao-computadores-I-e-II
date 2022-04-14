# Fatorial (recursão).

# define a função factorial() passando um argumento obrigatório
def factorial(a):

    # regra do fatorial para o número um
    if a == 1:
        return a

    # para todos os outros casos o número será ele mesmo vezes a própria função factorial()
    # passando como argumento o número que se deseja o fatorial menos um
    # observe que ao percorrer novamente a função e o número for finalmente igual a 01
    # entraremos na regra do fatorial e encerraremos a recursão
    return a * factorial(a-1)

# captura um número digitado pelo usuário
n = int(input("Digite um número: "))

# chamamos a função e imprimimos a mensagem com o retorno
print(f"O fatorial de {n} é: {factorial(n)}")