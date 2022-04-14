# Em qual quadrante está o ponto?

# Entradas
print("Digite as coordenadas de um ponto: ")
x = float(input("X ="))
y = float(input("Y ="))

# Condição
if x > 0 and y > 0:  # os dois valores são positivos
    print("1º quadrante")
elif x < 0 and y > 0:  # valor de x é negativo e y é positivo
    print("2º quadrante")
elif x < 0 and y < 0:  # valor de x e y são negativos
    print("3º quadrante")
elif x > 0 and y < 0:  # x positivo e y negativo
    print("4º quadrante")
elif x == 0 and y == 0:
    print("Origem")
