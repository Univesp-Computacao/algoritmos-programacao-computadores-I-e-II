# Defina, a função média(), que aceita dois
# números como entrada e retorna a média dos números. Um exemplo de uso é:
# >>> average(2, 3.5)

def average(a=int, b=int):
    "Função que retorna média entre dois valores a e b"
    try:
        return (a + b) / 2
    except:
        raise ValueError("Valor não inteiro")
    finally:
        print((a + b) / 2)

average(10,10) 
    # Output => 10.0
average(10, 4) 
    # Output => 7.0
average(4, 5) 
    # Output => 4.5
average(8, 10) 
    # Output => 9.0
