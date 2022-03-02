# Achar a equação da linha (y=kx+b) passando por dois pontos conhecidos.
# o problema é resolvido por sistema de equações onde k e b são constantes a serem encontradas
# convertidas na forma y = kx +b

# receber entradas
print("A(x1, y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("B(x2, y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Equação:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print (f"\ty = {k}*x + {b}")