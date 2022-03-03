# Determinar quando um ano é bissexto.
# entrada do ano
ano = int(input("Digite o ano:"))
# Condição
if ano % 4 != 0:
    print("ano comum")
elif ano % 100 == 0:
    if ano % 400 == 0:
        print("Ano Bissexto!")
    else:
        print("ano comum")
else:
    print("ano comum")
