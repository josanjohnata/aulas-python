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

# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" .
# 🦜 Uma dica: Utilize a função len() para verificar o tamanho do nome.


def find_biggest_name(names):
    biggest_name = names[0]
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
        return biggest_name

