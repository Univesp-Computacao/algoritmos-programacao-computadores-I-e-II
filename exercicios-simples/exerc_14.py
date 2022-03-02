# Em qual quadrante está o ponto?

# Entradas
print ("Digite as coordenadas de um ponto: ")
x = float(input("X ="))
y = float(input("Y ="))

#Condição
if x>0 and y>0:
    print("1º quadrante")
elif x<0 and y>0:
    print("2º quadrante")
elif x<0 and y<0:
    print("3º quadrante")
elif x>0 and y<0:
    print("4º quadrante")
elif x==0 and y==0:
    print("Origem")