# Dígitos estilizados com Unicode.

# As chaves do dicionário representam os dígitos
# os valores representam o código Unicode
digitos = {0: 9471, 1: 10102, 2: 10103, 3: 10104,
           4: 10105, 5: 10106, 6: 10107, 7: 10108,
           8: 10109, 9: 10110, 10: 10111}

# entrada de uma sequência numérica a ser transformada
sequencia = input("Digite uma sequência numérica: ")

# criando uma variavel para armazenar nova sequencia estilizada
nova_sequencia = ''

for i in sequencia:
    # converte para inteiro
    i = int(i)
    # extrai o código do dígito do dicionário e pega o caracter
    i = chr(digitos[i])


    nova_sequencia = nova_sequencia + i
print("Nova Sequência: ", nova_sequencia)
