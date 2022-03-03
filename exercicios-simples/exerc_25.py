# Selecionar inteiros de uma string.

texto_alfanumerico = input("Digite um texto alfanumérico: ")
tamanho_texto = len(texto_alfanumerico)
i = 0

while i < tamanho_texto:

    num = ''

    simbolo = texto_alfanumerico[i]

    while simbolo.isdigit():
        num += simbolo
        i += 1
        if i < tamanho_texto:
            simbolo = texto_alfanumerico[i]
        else:
            break
    if num != '':
        print(num)
    i += 1
