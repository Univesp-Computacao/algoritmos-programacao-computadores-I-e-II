# Achar a equação da linha (y=kx+b) passando por dois pontos conhecidos.

# A partir da entrada da coordenada de dois pontos (x,y), mostrar a equação
# que atravessa esses dois pontos.

# o problema é resolvido por sistema de equações:
# {y1 = kx1 + b ,e, y2 = kx2 + b}
# onde k e b são constantes a serem encontradas e x e y são dados
# convertidas na forma y = kx +b

# receber entradas
print("A(x1, y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("B(x2, y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Equação:")
# Achando o K de acordo com a fórmula
k = (y1 - y2) / (x1 - x2)

# Aplicando a fórmula
b = y2 - k * x2

print (f"\ty = {k}*x + {b}")