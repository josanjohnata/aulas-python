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

# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que lê todas essas informações e filtre mantendo somente as pessoas que estão reprovadas, e escreva seus nomes em outro arquivo. A nota miníma para aprovação é 6.

# Arquivo:
# Marcos 10
# Felipe 4
# José 6
# Ana 10
# Maria 9
# Miguel 5

recuStudents = []
with open("file.txt") as gradesFile:
    for line in gradesFile:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recuStudents.append(student_grade[0] + "\n")


with open("recuStudents.txt", mode="w") as recuStudentsFile:
    print(recuStudents)
    recuStudentsFile.writelines(recuStudents)
print(f"A soma dos valores válidos é: {sum}")
