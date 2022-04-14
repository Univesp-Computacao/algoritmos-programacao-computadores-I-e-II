# Calcular preço por quantidade de produtos.

# criação de um dicionário que recebe uma lista de elementos como valor para cada chave.
# o primeiro elemento da lista se refere ao valor e o segundo à quantidade
produtos = {'Maçã': [4.5, 10],
            'Laranja': [6.2, 5],
            'Abacaxi': [10.0, 1],
            'Manga': [7.50, 2],
            'Banana': [7.50, 2],
            }

# Atribuição de variáveis por tupla e método items(), específico da classe de objeto tipo Dict.

for chave, valor in produtos.items():
    # acessa os dados através do index da lista
    print(chave, '-', "preço:", valor[0], "qntd:", valor[1])

custo = 0

while True:
    # a variável produto irá armazenar em dado tipo str o nome da fruta desejada
    # neste caso temos que escrever exatamente igual ao valor que está na chave do dicionário
    produto = input("Qual fruta adicionar? (ou digite 'q' pra sair)")
    if produto == 'q':
        print("encerrando...")
        break
    qntd = int(input("Quantas unidades?"))
    if qntd > produtos[produto][1]:
        print("Não temos tudo isso.")
        continue
    custo += produtos[produto][0] * qntd
    produtos[produto][1] -= qntd

print("Total a pagar: ", custo)

for chave, valor in produtos.items():
    print(chave, '-', valor[0], valor[1])
