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
"""
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
"""

# Exercício 6.4
# O que acontece quando não verificamos se a lista está vazia antes de chamarmos o metodo pop?

# Resposta: Após remover todos os elementos, o programa apresentara um erro de indice:
# IndexError: pop from empty list

# Exercício 6.5
# Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez.
# Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação
# como uma string.
# Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente,
# a saida do programa

last = 3
queue = list(range(1, last + 1))

while True:
    print(f"\nThere are {len(queue)} customers in the queue")
    print(f"Current queue: {queue}")
    print("Type F to add a customer to the end of the queue,")
    print("or A to serve the next customer. Type S to exit.")

    i = 0
    operation = input("Operation (F, A, or S): ").upper()

    while i < len(operation):
        if operation[i] == 'A':
            if len(queue) > 0:
                served = queue.pop(0)
                print(f"Customer {served} has been served")
            else:
                print("Queue is empty! No one to serve.")
        elif operation[i] == 'F':
            last += 1
            queue.append(last)
        elif operation[i] == 'S':
            break
        else:
            print("Invalid operation! Please enter only F, A, or S.")
        i += 1

    print(f"Remaining queue: {queue}")

    if len(queue) == 0 or 'S' in operation:
        break

# Exercício 6.6
# Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho,
# considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2.
# O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2.

last_queue_one = 3
last_queue_two = 3
queue_one = list(range(1, last_queue_one + 1))
queue_two = list(range(1, last_queue_two + 1))
while True:
    print(f"\nThere are {len(queue_one)} customers in the queue one")
    print(f"\nThere are {len(queue_two)} customers in the queue two")
    print(f"Current queue one: {queue_one}")
    print(f"Current queue two: {queue_two}")
    print("""
    Type F to add a customer to the end of the queue one,
    or A to serve the next customer.
    Type G to add a customer to the end of the queue two,
    or B to serve the next customer.
    Type S to exit.
    """)

    operation = input("Operation (F, A, G, B or S):")
    if operation == 'A':
        if len(queue_one) > 0:
            served = queue_one.pop(0)
            print(f"Customer {served} in queue one has been served")
        else:
            print("Queue one is empty! No one to serve.")
    elif operation == 'F':
        last_queue_one += 1
        queue_one.append(last_queue_one)
    elif operation == 'B':
        if len(queue_two) > 0:
            served = queue_two.pop(0)
            print(f"Customer {served} in queue two has been served")
        else:
            print("Queue two is empty! No one to serve.")
    elif operation == "G":
        last_queue_two += 1
        queue_two.append(last_queue_two)
    elif operation == 'S':
        break
    else:
        print("Operação inválida! Digite apenas F, a ou S!")