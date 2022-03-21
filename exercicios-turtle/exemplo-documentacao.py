# Faz o desenho de um sol com contorno em vermelho e preenchimento em amarelo

# Faz o import do módulo Turtle
from turtle import *

# Escolhe as cores através da função color()
# A primeira cor será para o begin_fill() [contorno] e a segunda para o end_fill() [preenchimento]
color('red', 'yellow')

# A função begin_fill() deve ser iniciada logo antes da execução dos passos do desenho
begin_fill()

# Loop das instruções do desenho
while True:
    
    # avança 200
    forward(200)
    
    # gira 170º para a esquerda
    left(170)
    
    # quando a posição absoluta da tartaruga for menor que um, o loop é interrompido
    if abs(pos()) < 1:
        break
        
# Logo após a instrrução do desenho é feito o preenchimento        
end_fill()

# Programa encerrado
done()


"""
OBSERVAÇÃO:

Se dermos um print(pos()) logo após cada iteração do loope teremos o seguite resultado:

01.(200.00,0.00)
02.(3.04,34.73)
03.(190.98,-33.67)
04.(17.77,66.33)
05.(170.98,-62.23)
06.(42.42,90.98)
07.(142.42,-82.23)
08.(74.02,105.71)
09.(108.75,-91.25)
10.(108.75,108.75)
11.(74.02,-88.21)
12.(142.42,99.73)
13.(42.42,-73.48)
14.(170.98,79.73)
15.(17.77,-48.83)
16.(190.98,51.17)
17.(3.04,-17.23)
18.(200.00,17.50)
19.(0.00,17.50)
20.(196.96,-17.23)
21.(9.02,51.17)
22.(182.23,-48.83)
23.(29.02,79.73)
24.(157.58,-73.48)
25.(57.58,99.73)
26.(125.98,-88.21)
27.(91.25,108.75)
28.(91.25,-91.25)
29.(125.98,105.71)
30.(57.58,-82.23)
31.(157.58,90.98)
32.(29.02,-62.23)
33.(182.23,66.33)
34.(9.02,-33.67)
35.(196.96,34.73)
36.(0.00,-0.00)

Constatamos que foram realizadas 36 interações, que seria o resultado do total de grraus de uma circunferência (360º) dividido por 10º ( a diferença entre
180º - 170º).
"""
