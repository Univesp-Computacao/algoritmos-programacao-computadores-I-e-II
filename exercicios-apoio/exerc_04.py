# Desenvolver os diagramas de blocos e as codificações em português estruturado usando
# laço incondicional (para) do seguinte problema: Construir um programa que apresente a
# soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).

def exerc_04():
    "Soma dos 100 primeiros números naturais."
    conta = 0
    for i in range(101):
        conta = conta + i
    print("Exercício 4 é", conta)

exerc_04() # Output => Exercício 4 é 5050