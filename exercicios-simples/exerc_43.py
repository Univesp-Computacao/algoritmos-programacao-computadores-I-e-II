# Achar média de dois números usando funções

def media(n1,n2):
    media = (n1+n2)/2
    return media

a = int(input("A : "))
b = int(input("B : "))

resultado_media = media(a,b)
print(round(resultado_media,2))