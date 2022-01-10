# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def biggest_number(a, b):
    if a > b:
        return a
    return b

    print(biggest_number(4, 7))

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def average(list):
    media = 0
    for num in list:
        media += num
    return media / len(list)

