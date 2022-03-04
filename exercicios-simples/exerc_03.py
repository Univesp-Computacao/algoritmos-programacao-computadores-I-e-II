# Achar a área e o perímetro de um triângulo reto.
# importando um módulo nativo do python, que contém o método sqrt()
# que serve para extrair a raiz quadrada de um número.
import math

# Pede ao usuário que atribua valor aos catetos
# Como a função input() retorna uma string deve-se usar a função float()
# tornando o resultado final um número real
AB = float(input("Comprimento do primeiro cateto: "))
AC = float(input("Comprimento do segundo cateto: "))

# Calcula a hipotenusa através da extração da raiz da soma dos quadrados dos catetos
BC = math.sqrt(AB**2 + AC**2)

# A área de um triângulo reto é igual a metade da área correspondente ao seu retângulo
area = (AB*AC)/2

# Soma todos os lados
perimetro = AB + AC + BC

# Apresentando o valor usando f-string
print(f'Area do triângulo: {area} \n'
      f'Perímetro: {perimetro}')
