# Exercício 1: Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical.
NAME = input("Insira seu nome: ")
for letter in NAME:
    print(letter)

# OU

print("J")
print("O")
print("S")
print("A")
print("N")

# Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses valores. Caso algum valor da entrada seja inválido, por exemplo uma letra, uma mensagem deve ser exibida, na saída de erros, no seguinte formato: "Erro ao somar valores, {valor} é um valor inválido". Ao final, você deve imprimir a soma dos valores válidos.
numbers = input("Diginte um número: ")

numbersArr = numbers.split(" ")

sum = 0

for numbers in numbersArr:
    if not numbers.isdigit():
        print(f"Erro ao somar valores, {numbers} é um valor inválido")
    else:
        sum += int(numbers)

print(f"A soma dos valores válidos é: {sum}")
