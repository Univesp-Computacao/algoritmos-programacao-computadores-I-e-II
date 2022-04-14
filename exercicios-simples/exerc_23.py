# Achar uma equação quadrática que tenha soluções em uma faixa específica de coeficientes.
"""
Faixas de inteiros são entradas para os coeficientes a, b e c de uma equação quadrática.
Passa-se por todas combinações possíveis e determina para qual delas a equação tem raízes e para quais não tem.
Se possui raízes, então calcula.
Observar que quanto maior a distância entre os números maior será a lista de resultados.
Testar com valores a1:1, a2:3, b1:-1, b2:1, c1:-1, c2:1
"""
from math import sqrt

# Faixas para os coeficientes a, b e c
a1 = int(input('a1: '))
a2 = int(input('a2: '))
b1 = int(input('b1: '))
b2 = int(input('b2: '))
c1 = int(input('c1: '))
c2 = int(input('c2: '))

# Cria a faixa de objetos (o +1 permite chegar no limite da faixa)
a = range(a1, a2 + 1)
b = range(b1, b2 + 1)
c = range(c1, c2 + 1)

# Passa por todas as combinações possíveis de coeficientes
# 'i' é o item corrente na faixa do coeficiente 'a'
# 'j' é o item corrente na faixa do coeficiente 'b'
# 'k' é o item corrente na faixa do coeficiente 'c'
for i in a:
    if i == 0:
        # se o 'i'for igual a zero, a equação não é quadrática mas sim linear
        # portanto não é necessário resolvê-la, podendo passar para a próxima iteração no loop
        continue
    for j in b:
        for k in c:
            # O valor corrente de a, b e c são mostrados
            print(i, j, k, end=' ')

            # discriminante (delta)
            d = j * j - 4 * i * k

            # se o delta é positivo
            if d >= 0:

                # calculamos as raízes
                x1 = (-j - sqrt(d)) / (2 * i)
                x2 = (-j + sqrt(d)) / (2 * i)
                x1 = round(x1, 2)
                x2 = round(x2, 2)
                print("Sim, as raízes são:", x1, x2)

            # se delta é negativo:
            else:
                print("Não possui raízes")
