"""
Supondo que a variável previsão tenha recebido a string
'It will be a sunny day today'
escreva instruções Python correspondentes a estas atribuições:

  
A variável cont, a quantidade de ocorrências da string 'day' na string previsão.
A variável clima, o índice em que a substring 'sunny' começa.
A variável troca, uma cópia de previsão na qual cada ocorrência da substring
'sunny' é substituída por 'cloudy'.
"""

prevision = 'It will be a sunny day today'
count = prevision.count("day")
weather = prevision.index("sunny")
change = prevision.replace("sunny", "cloudy")

print(prevision)
    # Output => It will be a sunny day today
print(count)
    # Output => 2
print(weather)
    # Output => 13
print(change)
    # Output => It will be a cloudy day today
