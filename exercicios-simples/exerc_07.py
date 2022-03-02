# Determinar o número da letra no alfabeto.

# entrada de uma letra e transformação em minúscula
letra = input("Letra (A-Z): ").lower()

#definido o código da primeira letra do alfabeto
# a funçaõ ord() retorna o nº ordinal de um caractere no tabela símbolo
ordinal_a = ord('a')

# definindo ordinal da letra digitada
ordinal_letra = ord(letra)

#subtração da letra digitada pelo primeiro código, e adiciona um para encontrar o valor
numero = (ordinal_letra - ordinal_a) + 1


print(f'O numero referente a letra {letra} é o {numero}')

