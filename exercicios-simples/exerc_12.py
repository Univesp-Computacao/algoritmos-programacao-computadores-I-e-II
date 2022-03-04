# Convertendo Celsius para Farenheit

# Recebe a temperatura em Celsius
temperatura = float(input("Digite a temperatura em celsius"))

# Aplica a fórmula fazendo o areedondamento com o método round()
temperatura = round(temperatura * (9 / 5) + 32)

print(str(temperatura), 'F')
