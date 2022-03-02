# Calcular a soma de dígitos de um número randômico de 03 dígitos.

# importando o método random() do modulo random

from random import random

# obtendo um numero de três digitos (de 0 a 899)e adicionando 100 para chegar até a 999,
# e arredondado para não ter virgula
numero_randomico = round(random() * 900 + 100)

# extraindo o primeiro dígito usando o flood operator (//)

primeiro_digito = numero_randomico // 100

# extraindo segundo digito, dividindo por 10 e depois achando o resto por 10

segundo_digito = (numero_randomico // 10) % 10

# extraindo o terceiro dígito, apenas usando o modulos operato (%)

terceiro_digito = numero_randomico % 10

print(f'O número randômico é {numero_randomico}'
      f' a soma dos números é {primeiro_digito+segundo_digito+terceiro_digito}')
