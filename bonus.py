# Exercício 1: Dada uma lista, descubra o menor elemento. Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2 .


def minimum(numb):
    smaller = number[0]
    for number in numb:
        if number < smaller:
            smaller = number
    return smaller

# Dica: a função min já existe nativamente no Python! Trabalhando em Python, sempre compensa pesquisar uma solução primeiro porque este brinquedo vem com todos os acessórios inclusos!


def minimum2(numbers):
   return min(numbers)

# ou mesmo
minimum2 = min

# Exercício 2: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um triângulo retângulo com n asteriscos de base. Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:


def draw_triangle(n):
    for row in range(1, n + 1):
        print(row * '*')

# Exercício 3: Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N . Por exemplo, para N = 5 , o valor esperado será 15.


def summation(limit):
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total
