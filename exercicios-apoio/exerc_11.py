#Em que ordem os operadores nas expressões a seguir são avaliados?

# 2 + 3 == 4 or 5 >= 5
print("Ordem: +, ==, >=, or") 

# list[1] * -3 < -10 == 0
print("Ordem: *, <, ==")

# (list[1] * -3 < -10) in [0, True]
print("Ordem: *, <, in")

# 2 * 3**2
print("Ordem: **, *")

# 4 / 2 in [1, 2, 3]
print("Ordem: /, in")
