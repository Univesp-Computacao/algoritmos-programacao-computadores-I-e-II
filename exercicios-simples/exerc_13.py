# Calcular massa, densidade ou volume.

resultado = None

opcao = input("O que você quer calcular? (m, d, v):")
if opcao == 'm':
    densidade = float(input('Densidade:'))
    volume = float(input('Volume:'))
    resultado = densidade * volume
elif opcao == 'd':
    massa = float(input('Massa:'))
    volume = float(input('Volume:'))
    resultado = massa / volume
elif opcao == 'v':
    massa = float(input('Massa:'))
    densidade = float(input('Densidade:'))
    resultado = massa / densidade

print(resultado)