# Classificar palavras em uma string pelo número de caractéres (ascendente).

texto = input("Digite seu texto: ")
texto = texto.split()

texto.sort(key=len)

texto = ' '.join(texto)

print(texto)
