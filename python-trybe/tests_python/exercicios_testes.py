# Exercício 1: Escreva um programa que retorne uma lista com os valores
# numéricos de 1 a N, mas com as seguintes exceções :
# Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
# Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do
# número';
# Ex: 3 -> [1, 2, "Fizz"].

def fizzbuzz(n):
    numbers = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            numbers.append("FizzBuzz")
        elif number % 3 == 0:
            numbers.append("Fizz")
        elif number % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(number)
    return numbers

# Exercício 2: Em alguns lugares é comum lembrar um número do telefone
# associando seus dígitos a letras. Dessa maneira a expressão MY LOVE
# significa 69 5683. Claro que existem alguns problemas, uma vez que alguns
# números de telefone não formam uma palavra ou uma frase e os dígitos 1 e 0
# não estão associados a nenhuma letra.
# Sua tarefa é ler uma expressão e encontrar o número de telefone
# correspondente baseado na tabela abaixo. Uma expressão é composta por letras
# maiúsculas (A-Z), hifens (-) e os números 1 e 0.
# Exemplo:
# Letras  ->  Número
# ABC     ->  2
# DEF     ->  3
# GHI     ->  4
# JKL     ->  5
# MNO     ->  6
# PQRS    ->  7
# TUV     ->  8
# WXYZ    ->  9
# Curiosidade : A frase "The quick brown fox jumps over the lazy dog" é um
# pantograma (frase com sentido em que são usadas todas as letras do alfabeto
# de determinada língua) da língua inglesa.
# Verifique casos como entrada maior que 30 caracteres, vazia e com caracteres
# inválidos.


def translate_to_number(expression):
    if not 1 < len(expression) <= 30:
        raise ValueError("Expression with invalid length")
    number = ""
    for char in expression:
        if char in "ABC":
            number += "2"
        elif char in "DEF":
            number += "3"
        elif char in "GHI":
            number += "4"
        elif char in "JKL":
            number += "5"
        elif char in "MNO":
            number += "6"
        elif char in "PQRS":
            number += "7"
        elif char in "TUV":
            number += "8"
        elif char in "WXYZ":
            number += "9"
        elif char in "-01":
            number += char
        else:
            raise ValueError("Invalid character")
    return number

# Exercício 3: Faça uma função que valide um e-mail nos seguintes critérios
# abaixo, lançando uma exceção quando o valor for inválido. Endereços de email
# válidos devem seguir as seguintes regras:
# Devem seguir o formato nomeusuario@nomewebsite.extensao;
# O nome de usuário deve conter somente letras, dígitos, traços e underscores ;
# O nome de usuário deve iniciar com letra;
# O nome do website deve conter somente letras e dígitos;
# O tamanho máximo da extensão é três.
# As funções isalpha e isdigit podem ser utilizadas para verificar se uma letra
# ou palavra são compostas de somente caracteres ou dígitos.
# Exemplo : "1".isaplha() -> False , "a".isalpha() -> True


def validate_email(email):
    index = 0
    if not email[index].isalpha():
        raise ValueError("Username should starts with a letter")

    # validate username
    while email[index] != "@" and index < len(email):
        letter = email[index]
        if (
            not letter.isalpha()
            and not letter.isdigit()
            and letter not in ("_", "-")
        ):
            raise ValueError(
                "Username should contains only letters, "
                "digits, dashes or underscores"
            )
        index += 1
    index += 1  # @
    # validate website
    while email[index] != "." and index < len(email):
        letter = email[index]
        if not letter.isalpha() and not letter.isdigit():
            raise ValueError(
                "Website should contains only letters, and digits"
            )
        index += 1

    index += 1  # .
    # validate extension
    counter = 0
    while index < len(email):
        counter += 1
        index += 1
    if counter > 3:
        raise ValueError("Extension maximum length is 3")
    return None

# Exercício 4: Baseado no exercício anterior, escreva uma função que, dado uma
# lista de emails, deve retornar somente os emails válidos. Caso uma exceção
# ocorra, apenas a escreva na tela.
# Exemplo: ["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"] ->
# ["nome@dominio.com", "outro@dominio.com"]

def filter_valid_emails(emails):
    valid_emails = []
    for email in emails:
        try:
            validate_email(email)
        except ValueError as exc:
            print(exc)
        else:
            valid_emails.append(email)
    return valid_emails

