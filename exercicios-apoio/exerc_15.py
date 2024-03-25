import math
# Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo
# (um número não negativo) e retorna o perímetro do círculo. Você deverá escrever sua
# implementação em um módulo chamado perímetro.py. Um exemplo de uso é:

def perimetro(raio=int):
    if raio >= 0:
        return 2 * math.pi * raio
    else:
        raise ValueError("Valor menor que zero, por favor insira um valor diferente")

print(perimetro(0)) 
    # Output => 0.0
print(perimetro(1)) 
    # Output => 6.283185307179586
print(perimetro(2)) 
    # Output => 12.566370614359172