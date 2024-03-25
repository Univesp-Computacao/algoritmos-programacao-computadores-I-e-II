"""
Escreva uma função exer_36() que aceita duas listas bidimensionais do mesmo
tamanho (ou seja, o mesmo número de linhas e colunas) como argumentos de entrada e
incrementa cada entrada na primeira lista com o valor da entrada correspondente
na segunda lista.

            
>>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
>>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
>>> soma2D(t,s)
>>> for linha in t:
print(linha)

[4, 8, 4, 5]
[5, 2, 10, 3]
[8, 4, 6, 6]
"""

def exer_36(lista1=list, lista2=list):
    try:
        if (len(lista1) == len(lista2)):
            print(f"Lista 1: {lista1}")
            print(f"Lista 2: {lista2}")
            for i, rows in enumerate(lista1):
                for j, cols in enumerate(rows):
                    lista1[i][j] += lista2[i][j]
            print(f"Resultado: {lista1}")
    except:
        raise IndexError("Argumentos Inválidos")
    
# List 1
obj_1 = [[16, 64, 11, 38],[54, 41, 77, 2],[84, 55, 4, 88],[11, 80, 16, 48]]
obj_2 = [[36, 5, 43, 9],[48, 48, 96, 64],[85, 2, 16, 75],[91, 95, 22, 84]]

exer_36(obj_1, obj_2)
"""
Lista 1: [[16, 64, 11, 38], [54, 41, 77, 2], [84, 55, 4, 88], [11, 80, 16, 48]]
Lista 2: [[36, 5, 43, 9], [48, 48, 96, 64], [85, 2, 16, 75], [91, 95, 22, 84]]
Resultado: [[52, 69, 54, 47], [102, 89, 173, 66], [169, 57, 20, 163], [102, 175, 38, 132]]
"""