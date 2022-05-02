""""
Considere o seguinte trecho de código:
[Código]
O programa irá imrimir:
"""

def func(x, y):
    x, y = y, x


#   2, 3 = 3, 2


x = 2
y = 3

func(x, y)

# a função abaixo faz referência à variáveis globais
print(x, y)

# afunção irá imprimir  '2 3' pois as duas variáveis são globais
