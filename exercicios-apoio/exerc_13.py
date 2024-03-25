import math
import turtle

# Escreva expressões Python correspondentes ao seguinte:
# O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados
# têm comprimentos a e b

a = 4
b = 3
hip = math.sqrt(a**2 + b**2)
print(hip) 
    # Output => 5.0

# O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
Resultado = hip > 5
print(Resultado) 
    # Output => False

# A área de um disco com raio a
area = (math.pi * a**2)
print(area) 
    # Output => 50.26548245743669
print(round(area,2)) 
    # Output => 50.27

# O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está
# dentro de um círculo com centro ( a, b ) e raio r
x = 50
y = 49
print(f"x, y = {x, y}") 
    # Output => x, y = (50, 49)
a = 0
b = 0
print(f"a, b = {a, b}") 
    # Output => a, b = (0, 0)
r = 50

resultado = ((a - x)**2 + (b - y)**2 > r**2) 
print("(x,y) está fora círculo? Resposta:", resultado) 
    # Output => (x,y) está fora círculo? Resposta: True

# Visualmente
screen = turtle.Screen()
screen.setup(r*4, r*4)
circle_pen = turtle.Turtle(visible=False)
circle_pen.up()
circle_pen.setpos(0, -r)
circle_pen.down()
circle_pen.circle(radius=r)
xy_pos = turtle.Turtle(shape="circle")
xy_pos.color("#000", "#f00")
xy_pos.shapesize(0.2,0.2,0.2)
xy_pos.up()
xy_pos.setpos(x, y)
screen.mainloop()