# Achar a palavra mais longa de uma string.

texto = 'python java c c++ javascript pascal php'
print(texto)

# o método split() converte uma string em uma lista de palavras,
# usando " " (espaço) como separador.
palavras = texto.split()

# declara de início que a palavras mais longa é a primeira
id_mais_longa = 0

# as palavras são revistas em círculo e comparadas com a atual maior.
# Se alguma for maior "toma o lugar" e se torna a maior atual.
for i in range(1,len(palavras)):
    if len(palavras[id_mais_longa]) < len(palavras[i]):
        id_mais_longa = i

print(palavras[id_mais_longa])