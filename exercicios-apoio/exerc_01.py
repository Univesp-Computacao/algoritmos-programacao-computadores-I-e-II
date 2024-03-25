"""
Ler uma temperatura em graus Celsius e apresentá-la convertida
em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

def exerc_01(temperaturaC):
    " Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit."
    print("Em Farenheight é",(temperaturaC * 9 / 5) + 32, "°F.")
    return temperaturaC

exerc_01(0) # Output => Em Farenheight é 32 °F.
exerc_01(1) # Output => Em Farenheight é 33,8 °F.
exerc_01(10) # Output => Em Farenheight é 50 °F.
exerc_01(100) # Output => Em Farenheight é 212 °F.