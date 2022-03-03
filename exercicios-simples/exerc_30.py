# Achar a palavra mais longa de uma string.

texto = 'python java c c++ javascript pascal php'
print(texto)

palavras = texto.split()

id_mais_longa = 0

for i in range(1,len(palavras)):
    if len(palavras[id_mais_longa]) < len(palavras[i]):
        id_mais_longa = i

print(palavras[id_mais_longa])