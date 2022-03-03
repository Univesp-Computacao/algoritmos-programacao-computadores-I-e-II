# Calcular preço por quantidade de produtos.

# criação de um dicionário que recebe uma lista de dios elementos como valor.
produtos = {'Maçã': [4.5, 10],
            'Laranja': [6.2, 5],
            'Abacaxi': [10.0, 1],
            'Manga': [7.50, 2],
            'Banana': [7.50, 2],
            }

# Atribuição de variáveis por tupla e método items(), específico da classe de objeto tipo Dict.
for chave, valor in produtos.items():
    # acessa os dados através do index da lista
    print(chave, '-', valor[0], valor[1])

custo = 0

while True:
    produto = input("Qual fruta adicionar? (ou digite 'q' pra sair)")
    if produto == 'q':
        break
    qntd = int(input("Quantas unidades?"))
    if qntd > produtos[produto][1]:
        print("Não temos tudo isso.")
        continue
    custo += produtos[produto][0] * qntd
    produtos[produto][1] -= qntd

print("Preço: ", custo)

for chave, valor in produtos.items():
    print(chave, '-', valor[0], valor[1])