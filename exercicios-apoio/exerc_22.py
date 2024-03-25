# Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True,
# exiba 'Posso escapar.'.

def Exercicio32d(**pontos_cardeais):
    if True in pontos_cardeais.values():
        print("Posso escapar.")
        
Exercicio32d(norte=True,sul=True,leste=True,oeste=True)
