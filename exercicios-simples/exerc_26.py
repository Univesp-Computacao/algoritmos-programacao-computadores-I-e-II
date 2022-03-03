# Determinar a porcentagem de minúsculas e maiúsculas de uma string.

texto = input("Digite seu texto: ")

tam_texto = len(texto)

# múltipla atribuição
minusculas = maiusculas = 0

for i in texto:
    if i.islower():
        minusculas +=1
    elif i.isupper():
        maiusculas +=1

porcent_minusculas = minusculas / tam_texto * 100
porcent_maiusculas = maiusculas / tam_texto * 100
print (f"Porcentagem mínusculas: {porcent_minusculas} e porcentagem maiusculas: {porcent_maiusculas}")
