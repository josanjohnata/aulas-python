# Exercício 1: Dado um array de números de tamanho n , escreva um algoritmo que
# retorna true se há no array um número duplicado e false caso contrário.
# Analise a solução abaixo e diga qual é a ordem de complexidade desse
# algoritmo para o melhor caso, pior caso e caso médio.


""" O algoritmo ordena o array independente de qualquer coisa, então
o seu pior caso, melhor caso e caso médio são, no mínimo,
complexidade do algoritmo de ordenação do Python. Vendo a documentação,
vemos que tal algoritmo é O(n log n). Dado que, depois de ordenar, no pior
caso passamos pelo array inteiro uma vez só, isso seria O(n). Assim sendo,
a complexidade é O(n*log(n) + n) o que, simplificando, fica O(n log n)"""


def contains_duplicate(numbers):
    numbers.sort()
    previous_number = 'not a number'
    for number in numbers:
        if(previous_number == number):
            return True
        previous_number = number

    return False


# Exercício 2: Suponha que se está escrevendo uma função para um jogo de
# batalha naval. Dado um array bidimensional com n linhas e m colunas, e um
# par de coordenadas x para linhas e y para colunas, o algoritmo verifica se
# há um navio na coordenada alvo. Por exemplo:


""" Mesmo para um array bidimensional, o acesso a um elemento é O(1).
A complexidade de espaço também é O(1), pois não consideramos a entrada em seu
cálculo."""

"""
entrada = [ 0 0 0 0 1
 0 0 0 1
 1 1 1 1
 0 0 1 0 ]

resultado para (0, 4) = True
resultado para (1, 1) = False
"""


def battleship(grid, line, column):
    if(grid[line][column] == 1):
        return True

    return False
