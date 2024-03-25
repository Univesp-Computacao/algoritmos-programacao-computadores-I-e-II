# Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python ou
# instruções que mapeiam o primeiro e último valor da lista. Assim, se a lista
# original for:

# >>> time = ["Ava", "Eleanor", "Clare", "Sarah"]
  
# então a lista resultante deverá ser:
  
# >>> time
# ["Sarah", "Eleanor", "Clare", "Ava"]

def exerc_18(args):
    if len(args) > 1:
        firstItem = args[0]
        lastItem = args[-1]
        args[0] = lastItem
        args[-1] = firstItem
        return args
    else:
        raise IndexError("Lista menor que 1.")

print(exerc_18([0,2,3,4,5,6,7]))
    # Output => [7, 2, 3, 4, 5, 6, 0]

print(exerc_18(["Sarah", "Eleanor", "Clare", "Ava"]))
    # Output => ['Ava', 'Eleanor', 'Clare', 'Sarah']

print(exerc_18([True,False,True,False]))
    # Output => [False, False, True, True]

print(exerc_18([True,False]))
    # Output => [False, True]

print(exerc_18([True]))
    # Output => IndexError: Lista menor que 1.