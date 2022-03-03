# Disribuir valores por faixa.

a = [3, 5, 7, 3, 8, 1, 8, 1, 7, 3, 2, 4, 6, 8, 5, 4, 3, 3, 6, 5, 7, 8, 9, 5, 3, 2, 3]

cont_1_3 = 0
cont_4_6 = 0
cont_7_9 = 0

for i in a:
    if 1 <= i <= 3:
        cont_1_3 += 1
    elif 4 <= i <= 6:
        cont_4_6 += 1
    elif 7 <= i <= 9:
        cont_7_9 += 1

print(f' Na faixa de 1 a 3 temos: {cont_1_3} itens')
print(f' Na faixa de 4 a 6 temos: {cont_4_6} itens')
print(f' Na faixa de 7 a 9 temos: {cont_7_9} itens')
