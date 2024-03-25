# Dada a lista de notas de trabalho de casa dos alunos

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# Escreva: 
print("Uma expressão que avalia para o número de 7 notas.")
print(notas.count(7)) 
    # Output => 2

print("Uma instrução que muda a última nota para 4.")
notas[-1] = 4
print(notas) 
    # Output => [9, 7, 7, 10, 3, 9, 6, 6, 4]

print("Uma expressão que avalia para a nota mais alta.")
print(max(notas)) 
    # Output => [9, 7, 7, 10, 3, 9, 6, 6, 4]

print("Uma instrução que classifica as notas da lista.")
notas.sort()
print(notas) 
    # Output => [9, 7, 7, 10, 3, 9, 6, 6, 4]

print("Uma expressão que avalia para a média das notas.")
print(sum(notas) / len(notas)) 
print(sum(notas) // len(notas))
    # Output => [9, 7, 7, 10, 3, 9, 6, 6, 4]
    # Output => [9, 7, 7, 10, 3, 9, 6, 6, 4]
