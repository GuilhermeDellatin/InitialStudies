# Programa 6.1 Calculo da media
#
# notas = [6, 7, 5, 8, 9]
# soma = 0
# x = 0
# while x < 5:
#    soma += notas[x]
#    x += 1
# print(f"Média: {soma / x:5.2f}")

# Programa 6.2 Calculo da media com notas digitadas
#
# notas = [0, 0, 0, 0, 0]
# soma = 0
# x = 0
# while x < 5:
#    notas[x] = int(input(f"Nota {x}: "))
#    soma += notas[x]
#    x += 1
# x = 0
# while x < 5:
#    print(f"Nota {x}: {notas[x]:6.2f}")
#    x += 1
# print(f"Media: {soma / x:5.2f}")

# Exercício 6.1
# Modifique o Programa 6.2 para ler 7 notas em vez de 5.

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
# while True:
#    element = input("Enter the first list elements, enter x to stop: ")
#
#    if element == 'x':
#        break
#    elif element == '':
#        print("Invalid element")
#    else:
#        first_list.append(element)
#
# while True:
#    element = input("Enter the second list elements, enter 0 to stop: ")
#    if element == 'x':
#        break
#    elif element == '':
#        print("Invalid element")
#    else:
#        second_list.append(element)
# Também funciona da forma abaixo, porém cria uma lista temporaria e concatena na lista original
#        second_list += [element]

# Exercício 6.3
# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

"""
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
"""

# Better code with while:

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

combined_list = first_list + second_list
unique_list = []
i = 0

while i < len(combined_list):
    if combined_list[i] not in unique_list:
        unique_list.append(combined_list[i])
    i += 1

print(f"The result list without duplicates element is {unique_list}")

# Programa 6.8 Simulação de uma fila de banco

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")

    operacao = input("Operação (F, A ou S):")
    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif operacao == 'S':
        break
    else:
        print("Operação inválida! Digite apenas F, a ou S!")