# Saída dos caracteres da tabela ASCII.
# Mostrar em uma tabela os carcteres de 32 a 127, inclusive.

# Na tabela de símbolos , os números, as letras, as pontuações
# todos possuem um índice.

# Com a função range(32,128) criamos índices de 32 a 127
# e com o for podeos fazer a iteração de item a item.
for i in range(32,128):
    # A função chr() retorna u caracter quando seu código
    # é passado como argumento.
    print(chr(i), end=' ')
    if (i -1)%10==0:
        print()
print()