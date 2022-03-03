# Dígitos estilizados com Unicode.

digitos = {0: 9471, 1: 10102, 2: 10103, 3: 10104,
           4: 10105, 5: 10106, 6: 10107, 7: 10108,
           8: 10109, 9: 10110, 10: 10111}
n = input("Digite uma sequência numérica: ")

novo_n = ''

for i in n:
    i = int(i)
    i = chr(digitos[i])
    novo_n = novo_n + i
print(novo_n)
