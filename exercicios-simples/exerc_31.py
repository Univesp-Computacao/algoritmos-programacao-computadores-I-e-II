# Converter um texto para uma lista de palavras sem pontuação.
texto = input("Digite um texto: ")
pontuacao = ['.', ',', ':', ';', '!', '?', '(', ')']

palavras = texto.split()

i = 0
for palavra in palavras:
    if palavra[-1] in pontuacao:
        palavras[i] = palavra[:-1]
        palavra = palavras[i]
    if palavra[0] in pontuacao:
        palavras[i] = palavra[1:]
    i += 1

for i in palavras:
    print(i, end=' ')
print()