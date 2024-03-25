"""
Traduza estas declarações em instruções if/else do Python:

Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário,
exiba 'Definitivamente não é um ano bissexto.'
"""
def exerc_23(ano=int):
    if (ano % 4 == 0):
        print("Pode ser um ano bissexto.")
    else:
        print("Definitivamente não é um ano bissexto.")

exerc_23(2013)
    # Output => Definitivamente não é um ano bissexto.
exerc_23(1990)
    # Output => Definitivamente não é um ano bissexto.
exerc_23(1994)
    # Output => Definitivamente não é um ano bissexto.
exerc_23(2024)
    # Output => Pode ser um ano bissexto.
exerc_23(2004)
    # Output => Pode ser um ano bissexto.
exerc_23(2010)
    # Output => Definitivamente não é um ano bissexto.
exerc_23(2008)
    # Output => Pode ser um ano bissexto.
exerc_23(2003)
    # Output => Definitivamente não é um ano bissexto.
