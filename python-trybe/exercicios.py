# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def biggest_number(a, b):
    if a > b:
        return a
    return b

    print(biggest_number(4, 7))

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.


def average(list):
    total = 0
    for num in list:
        total += num
    return total / len(list)

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n.


def draw_square(n):
    for row in range(n):
        print(n * '*')

