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