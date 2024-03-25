"""
Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
A soma de 2 e 2 é menor que 4.
O valor de 7 // 3 é igual a 1 + 1.
A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
A soma de 2, 4 e 6 é maior que 12.
1387 é divisível por 19.
31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
"""

def exerc_06(a, b, c):
    "Função comparativa"
    match c:
        case ">=":
            print(a >= b)
            return a >= b
        case "<=":
            print(a <= b)
            return a <= b
        case ">":
            print(a > b)
            return a > b
        case "<":
            print(a < b)
            return a < b
        case "==":
            print(a == b)
            return a == b
        case "!=":
            print(a != b)
            return a != b


# A soma de 2 e 2 é menor que 4. 
exerc_06(2+2, 4, "<")  
# Output => False

# O valor de 7 // 3 é igual a 1 + 1. 
exerc_06(7//3, 1+1, "==") 
# Output => True

# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25. 
exerc_06((3**2)+(4**2), 25, "==") 
# Output => True

# A soma de 2, 4 e 6 é maior que 12.
exerc_06(2+4+6, 12, ">") 
# Output => False

# 1387 é divisível por 19.
exerc_06(1387%19, 0, "==") 
# Output => True

# 31 é par.
exerc_06(31%2, 0, "==") 
# Output => False

# O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.
exerc_06(min([34.99, 29.95, 31.50]), 30, "<") 
# Output => True
