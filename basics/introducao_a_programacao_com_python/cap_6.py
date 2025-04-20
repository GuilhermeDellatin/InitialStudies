# Programa 6.1 Calculo da media
#
#notas = [6, 7, 5, 8, 9]
#soma = 0
#x = 0
#while x < 5:
#    soma += notas[x]
#    x += 1
#print(f"Média: {soma / x:5.2f}")

# Programa 6.2 Calculo da media com notas digitadas
#
#notas = [0, 0, 0, 0, 0]
#soma = 0
#x = 0
#while x < 5:
#    notas[x] = int(input(f"Nota {x}: "))
#    soma += notas[x]
#    x += 1
#x = 0
#while x < 5:
#    print(f"Nota {x}: {notas[x]:6.2f}")
#    x += 1
#print(f"Media: {soma / x:5.2f}")

# Exercício 6.1
# Modifique o Programa 6.2 para ler 7 notas em vez de 5.
"""
grades = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
sum_grades = 0
grade = 0

while grade < 7:
    grades[grade] = float(input(f"Grade {grade}: "))
    sum_grades += grades[grade]
    grade += 1

grade = 0

while grade < 7:
    print(f"Grade {grade}: {grades[grade]:6.2f}")
    grade += 1

print(f"Average: {sum_grades / grade:5.2f}")

# Exercício 6.2
# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

first_list = []
second_list = []

while True:
    element = int(input("Enter the first list elements, enter 0 to stop: "))

    if element == 0:
        break
    else:
        first_list.append(element)

while True:
    element = int(input("Enter the second list elements, enter 0 to stop: "))
    if element == 0:
        break
    else:
        second_list.append(element)
#       Também funciona da forma abaixo, porém cria uma lista temporaria e concatena na lista original
#       second_list += [element]
# Garante que nenhuma lista seja referenciada diretamente
# third_list = first_list[:] + second_list[:]

# Como não vamos usar essa lista adiante nesse cenário está ótimo para juntar listas.
third_list = first_list + second_list
print(f"third_list = {third_list}")

# Se quisermos que permita qualquer input, só substituir o trecho de código da repetição pelo trecho a seguir:
#
#while True:
#    element = input("Enter the first list elements, enter x to stop: ")
#
#    if element == 'x':
#        break
#    elif element == '':
#        print("Invalid element")
#    else:
#        first_list.append(element)
#
#while True:
#    element = input("Enter the second list elements, enter 0 to stop: ")
#    if element == 'x':
#        break
#    elif element == '':
#        print("Invalid element")
#    else:
#        second_list.append(element)
#Também funciona da forma abaixo, porém cria uma lista temporaria e concatena na lista original
#        second_list += [element]
"""
from shutil import which

# Exercício 6.3
# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

first_list = []
second_list = []

while True:
    element = int(input("Enter the first list elements, enter 0 to stop: "))

    if element == 0:
        break
    else:
        first_list.append(element)

while True:
    element = int(input("Enter the second list elements, enter 0 to stop: "))
    if element == 0:
        break
    else:
        second_list.append(element)

third_list = first_list[:] + second_list[:]
third_list_without_repeat = []
x = 0

while x < len(third_list):
    y = 0

    while y < len(third_list_without_repeat):

        if third_list[x] == third_list_without_repeat[y]:
            break
        y += 1

    if y == len(third_list_without_repeat):
        third_list_without_repeat.append(third_list[x])
    x += 1

print(third_list_without_repeat)