# Criar dicionário de duas listas.

lista_a = [1,2,3,4,5]
lista_b= ['a','b','c','d','e']


lista_c = {}
for i in range(len(lista_a)):
    lista_c[lista_b[i]] = lista_a[i]

print(lista_c)
print(type(lista_c))
