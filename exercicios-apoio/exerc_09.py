"Pegando de índices em listas."
# Primeiro, execute a atribuição
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

# Agora, escreva duas expressões Python que são avaliadas, respectivamente,
# como a primeiro e a última palavras em palavras, na ordem do dicionário.

palavras.sort() 
    # Output => ['bola', 'celeiro', 'cesta', 'peteca', 'taco']
print(f"{palavras[0]}, {palavras[-1]}") 
    # Output => bola,taco
