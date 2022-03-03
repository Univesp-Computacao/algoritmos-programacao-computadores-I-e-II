# Inverter a ordem de uma string.

def inverterPalavras(texto):
    texto = texto.split()
    texto.reverse()
    return ' '.join(texto)
print(inverterPalavras(input("Digite um texto:")))
