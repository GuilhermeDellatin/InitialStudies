import math

# Exercício 3.1
# Elabore um algoritmo que calculem quantas notas de 50, 10 e 1 são necessárias para pagar uma conta
# cujo valor é fornecido.

# Simple solution and one form for interpret the problem:
"""
account_value = int(input("Enter the account value: "))

quantity_of_notes_fifty = rest_value // 50
quantity_of_notes_ten = rest_value // 10
quantity_of_notes_one = rest_value // 1

print(f'''
To pay the account in value of {account_value}
Its necessary {quantity_of_notes_fifty} of notes of fifty
Its necessary {quantity_of_notes_ten} of notes of ten
Its necessary {quantity_of_notes_one} of notes of one
''')
"""

# Another solution and interpret the problem:
account_value = int(input("Enter the account value: "))
rest_value = account_value

quantity_of_notes_fifty = rest_value // 50
rest_value %= 50
quantity_of_notes_ten = rest_value // 10
rest_value %= 10
quantity_of_notes_one = rest_value // 1

print(f'''
To pay the account in value of {account_value}
Its necessary {quantity_of_notes_fifty} of notes of fifty
Its necessary {quantity_of_notes_ten} of notes of ten
Its necessary {quantity_of_notes_one} of notes of one
''')

# Exercício  3.5
# Elabore um algoritmo que calcule o alcance de um projetil, dada a velocidade inicial v0 e angulo Theta entre o
# cano do canhão e o solo. A fórmula a ser utilizada é:
# S = (v0²/g) * sen(2teta)

initial_velocity = float(input("Enter initial velocity: "))
theta_angle = float(input("Enter the angle of projectile: "))

distance = (initial_velocity / 10) * math.sin(2 * theta_angle)

print(f"The distance of projectile is: {distance:.3f}, the formula to calcule this is  S = (v0²/g) * sen(2teta)")
# Exercício 3.6
# Elabore um algoritmo que calcula a área de um triângulo pela fórmula de Hierão:
# K = SQRT(s(s - a) * (s - b) * (s - c))
# Em que K é a área do triângulo, s o semiperímetro e a, b e c os lados do triângulo.

side_a = int(input("Enter the side a: "))
side_b = int(input("Enter the side b: "))
side_c = int(input("Enter the side c: "))
semi_perimeter = (side_a + side_b + side_c) / 2

hieron = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))

print(f"The result is {hieron:.2f}")

# Exercício 3.7
# Elabore um algoritmo que permitam a entrada de um número inteiro e diga se ele é par ou ímpar.

number = int(input("Enter the number to verify he is even or odd: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Exercício 3.8
# Elabora um algoritmo que leia dois numeros (x e y) e escreva como resultado o maior entre deles

number_x = int(input("Enter the number x: "))
number_y = int(input("Enter the number y: "))

if number_x > number_y:
    print(f"The number {number_x}  is greater than {number_y}")
elif number_y > number_x:
    print(f"The number {number_y}  is greater than {number_x}")
else:
    print(f"The number {number_x}  is equal than {number_y}")

# Exercício 3.9
# Elabora um algoritmo que permite a entrada de dois valores, x e y, troque seus valores entre si e então exiba os
# novos resultados.

# Observação, reaproveitando os inputs do exercício anterior
print(f"Number x is {number_x} and Number y is {number_y}")
number_swapped = number_x
number_x = number_y
number_y = number_swapped

print(f"Swapped values, Number x is {number_x} and Number y is {number_y}")

# Exercício 3.11
# Elabore um algoritmo que permita a entrada de n valores reais e apresente como resultado o maior deles

number_list = []

while True:
    number = int(input("Enter a number or 0 to exit: "))
    if number == 0:
        break
    else:
        number_list.append(number)

print(f"The biggest number is {max(number_list)}")

# Exercício 3.12
# Idem ao exercício 3.8, só que escreva o menor deles

# Exercício 3.13
# Elabore um algoritmo que calcule e exiba a media de dois números digitados