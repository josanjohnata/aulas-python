# Exercícios de fixação


# Exercício 1: Fibonacci: Ligue o cronômetro, e faça a medição de quanto tempo
# você leva para resolver este problema. Se demorar mais de 10 minutos, pare!
# Seu tempo acabou.


def fibonacci1(n):
    sequence = [0, 1]
    for x in range(n):
        next = sequence[-1] + sequence[-2]
        sequence.append(next)
    return sequence[-1]

# Na forma iterativa, calculamos todos os números da sequência até o número
# desejado.


def fibonacci2(n):
    if n < 2:
        return n
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)


# Exercício 2: ReverseCorp Ligue seu cronômetro de novo, e tente desenvolver
# esta solução, utilizando a iteração. (Se demorar mais que 10 minutos, pare,
# e prossiga com o conteúdo!)

"""
Nesta solução iterativa, percorremos a lista inserindo seus elementos em uma
nova lista, porém a inserção ocorre no começo da lista (posição 0) assim a
ordem se inverte.
"""


def reverse1(list):
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
    return reversed_list


"""
Nesta solução recursiva primeiro definimos a condição de parada, ou caso base:
se a lista tiver menos de dois elementos, ela invertida será ela mesma.
Depois, a lógica de recursão é: Para inverter uma lista, basta colocar o
primeiro elemento no fim, e depois inverter o resto da lista.
"""


def reverse2(list):
    if len(list) < 2:
        return list
    else:
        return reverse2(list[1:]) + [list[0]]


# Exercício 3: Faça um algoritmo recursivo de soma. Esse algoritmo deve
# receber um número de parâmetro e deve somar todos os números antecessores a
# ele.

def sum_recursive(n):  # nome da função e parâmetro
    if n == 0:  # condição de parada
        return 0

    else:
        return n + sum_recursive(n - 1)
        # chamada de si mesma com um novo valor


sum_recursive(4)

#####################################################################

# Exercício 1: Crie um algoritmo não recursivo para contar quantos números
# pares existem em uma sequência numérica (1 a n).


def conta_pares(n):
    numero_de_pares = 0
    for num in range(n+1):
        if num % 2 == 0 and num != 0:
            numero_de_pares += 1
    return numero_de_pares

# Exercício 2: Transforme o algoritmo criado acima em recursivo.
# Exercício 3: Crie um algoritmo recursivo que encontre, em uma lista, o maior
# número inteiro.
# Exercício 4: Escreva um algoritmo recursivo para encontrar o máximo divisor
# comum (mdc) de dois inteiros.
# Exercício 5: Escreva um algoritmo recursivo que identifica se um número é
# primo.

#########################################################################

# Bônus
# Exercício 6: Escreva um algoritmo recursivo que resolva o problema da torre
# de hanoi, seguindo as instruções:
# Assim como na imagem abaixo, a torre deve conter 3 discos, e três colunas;
# Os discos começam alinhados na primeira coluna, e devem ser organizados respeitando a ordem de tamanho, na última coluna.