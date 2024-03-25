"""
Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa
(em metros) e o peso (em quilos) e calcula o Índice de Massa Corporal (IMC)
dessa pessoa. A fórmula do IMC é:.
Sua função deverá exibir a string 'Abaixo do peso' se o imc < 18.5,
'Normal' se 18,5 <= imc < 25, e
'Sobrepeso' se imc >= 25.
  
>>> meuIMC(86, 1.90)
Normal
>>> meuIMC(63, 1.90)
Abaixo do peso
"""

def exerc_26(weight=int,height=float):
    imc = weight/(height**2)
    if (imc < 18.5):
        print('Abaixo do peso')
    elif (imc >= 18.5 and imc <= 25):
        print('Normal')
    else:
        print('Sobrepeso')

exerc_26(68, 1.69)
    # Output => Normal