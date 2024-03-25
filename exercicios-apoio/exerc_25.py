"""
Implemente um programa que comece pedindo ao usuário para digitar uma identificação
de login (ou seja, uma string). O programa, então, verifica se a identificação
informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários
válidos. Dependendo do resultado, uma mensagem apropriada deverá ser impressa. Não
importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.
Aqui está um exemplo de um login bem-sucedido:
  
>>>
Login: joe
Você entrou!
Fim.

E aqui está um que não tem sucesso:

>>>
Login: john
Usuário desconhecido.
Fim.
"""

def exerc_25(user=str):
    if (user in ['joe', 'sue', 'hani', 'sophie' ]):
        print("Logado com Sucesso")
    else:
        print("Usuário desconhecido")

exerc_25(input("Login:"))