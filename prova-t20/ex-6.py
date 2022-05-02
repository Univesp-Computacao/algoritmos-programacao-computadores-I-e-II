"""
Implemente uma função em Python que receba uma string como parâmetro e imprima
 as vogais dessa string. Exemplo: string ‘univesp’ →deve imprimir os caracteres
 ‘u’, ‘i’ e ‘e’.
"""


def vogais(str):
    for i in range(len(str)):
        if str[i] in 'aeiouAEIOU':
            print(str[i])


vogais('univesp')
