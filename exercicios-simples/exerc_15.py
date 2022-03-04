# Determinar quando um ano é bissexto a partir da entrada de um ano.

# • De quatro em quatro anos ocorre o ano bissexto.
# • De 100 em 100 anos não ocorre o ano bissexto.
# • De 400 em 400 anos ocorre o ano bissexto.
# • As últimas regras prevalecem sobre as primeiras.


ano = int(input("Digite o ano:"))
# Condição

# excluindo os anos que não são bissextos
if ano % 4 != 0:
    print("ano comum")
# dando as condições de quando um ano é bissexto
elif ano % 100 == 0:
    if ano % 400 == 0:
        print("Ano Bissexto!")
    else:
        print("ano comum")
# Nos outros casos é ano comum
else:
    print("ano comum")
