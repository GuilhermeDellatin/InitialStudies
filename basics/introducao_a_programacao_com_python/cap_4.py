# Listagem 4.2 - Condições
#
# a = int(input("Primeiro Valor: "))
# b = int(input("Segundo Valor: "))
# if a > b:
#   print("O primeiro número é o maior!")
# if b > a:
#   print("O segundo número é o maior!")
from basics.introducao_a_programacao_com_python.cap_2 import result

# Exercício 4.1
# Analise o programa da listagem 4.2. Responda o que acontece
# se o primeiro e o segundo valores forem iguais? Explique.

a = int(input("First Value: "))
b = int(input("Second Value: "))
if a > b:
    print("The first value is the biggest!")
if b > a:
    print("The second value is the biggest!")

# Resposta:
# Quando os dois valores são iguais nenhuma instrução print é executada pois não satisfazem as condições if

# Exercício 4.2
# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h,
# exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando
# R$ 5 por km acima de 80km/h

car_velocity = int(input("What is your speed?: "))
if car_velocity > 80:
    fine = (car_velocity - 80) * 5
    print("You were fined, and its value is: R$", fine)

# Exercício 4.3
# Escreva um programa que leia três números e que imprima o maior e o menor

# Obs: Resolvendo apenas com if nesse momento
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

bigger = first_number
smaller = first_number

if second_number > bigger:
    bigger = second_number
if third_number > bigger:
    bigger = third_number

if second_number < smaller:
    smaller = second_number
if third_number < smaller:
    smaller = third_number

print("The biggest number is %d and the smaller is %d" % (bigger, smaller))

# Exercício 4.4
# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores
# ou iguais, de 15%.

employee_salary = float(input("Enter your salary to calcule your increase:"))
increase = 0

if employee_salary > 1250:
    increase = employee_salary * 0.1
if employee_salary <= 1250:
    increase = employee_salary * 0.15

print("The value of increase is: %.2f" % increase)

# Exercício 4.5
# Execute o programa (Listagem 4.5) e experimente alguns valores.
# Verifique se os resultados foram os mesmos do programa anterior (Listagem 4.3)

# Listagem 4.3 - Carro novo ou velho, dependendo da idade:
# idade = int(input("Digite a idade do seu carro: "))
# if idade <= 3:
#   print("Seu carro é novo")
# if idade > 3:
#   print("Seu carro é velho")

# Listagem 4.5 - Carro novo ou velho, dependendo da idade com else
# idade = int(input("Digite a idade do seu carro: "))
# if idade <= 3:
#   print("Seu carro é novo")
# else:
#   print("Seu carro é velho")

car_age = int(input("Enter the car age: "))
if car_age <= 3:
    print("Your car is new")
else:
    print("Your car is old")

# Resposta:
# Os resultados foram os mesmos nesse caso, porém usando o else
# quando o if não é satisfeito o bloco else é executado
# já no primeiro caso usando dois ifs é feito outra verificação
# para verificar a condição do segundo if

# Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro
# deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens de até 200 km, e R$ 0,45 para viagens mais longas

passenger_travel_distance = float(input("What distance you travel in km?: "))

if passenger_travel_distance <= 200:
    ticket_price = passenger_travel_distance * 0.50
else:
    ticket_price = passenger_travel_distance * 0.45

print("The Ticket price is %.2f" % ticket_price)

# Uma forma outra forma de resolver:
# ticket_price = passenger_travel_distance * (0.50 if passenger_travel_distance <= 200 else 0.45)

# Listagem 4.7 - Categoria x preço

# categoria = int(input("Digite a categoria do produto: "))
#
# if categoria == 1:
#    preco = 10
# else:
#    if categoria == 2:
#        preco = 18
#    else:
#        if categoria == 3:
#            preco = 23
#        else:
#            if categoria == 4:
#                preco = 26
#            else:
#                if categoria == 5:
#                    preco = 31
#                else:
#                    print("Categoria inválida, digite um valor entre 1 ee 5!")
#                    preco = 0
#
# print("O preço do produto é: R$%6.2f" % preco)

# Exercício  4.7
# Rastreie o programa da listagem 4.7. Compare seu resultado ao apresentado na tabela 4.2

# Resposta:
# Entrada = 0 -> 120,122,124,125,127,128,130,131,133,134,136,137,138,140
# Entrada = 1 -> 120,122,123,140
# Entrada = 2 -> 120,122,124,125,126,140
# Entrada = 3 -> 120,122,124,125,127,128,129,140
# Entrada = 4 -> 120,122,124,125,127,128,130,131,132,140
# Entrada = 5 -> 120,122,124,125,127,128,130,131,133,134,135,140
# Entrada = 9 -> 120,122,124,125,127,128,130,131,133,134,136,137,138,140

# Exercício 4.8
# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar
# Você pode calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado
# da operação solicitada

number_one = float(input("Enter number one: "))
number_two = float(input("Enter number two: "))
operation = input("Enter operation: ")

if operation == '+':
    result = number_one + number_two
elif operation == '-':
    result = number_one - number_two
elif operation == '*':
    result = number_one * number_two
elif operation == '/':
    result = number_one / number_two
else:
    print("Invalid operation!")

print("The result of operation %s of the numbers %.2f and %.2f is: %.2f" % (operation, number_one, number_two, result))

# Exercício 4.9
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve
# perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação
# mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa
# a comprar dividido pelo número de meses a pagar

house_value = float(input("Enter the value of the house you want to buy: "))
salary_receive = float(input("Enter your salary: "))
months_to_pay = int(input("Enter the quantity of months to pay: "))
installment = house_value / months_to_pay

if installment <= salary_receive * 0.30:
    print("The loan is approved, and  your installment is: %.2f" % installment)
else:
    print("The loan is reproved")

# Exercício 4.10
# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade
# de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir.
#
# Preço por tipo e faixa de consumo
# Tipo              Faixa           Preço
#
# Residencial     Até 500           R$ 0,40
#               Acima de 500        R$ 0,65
# Comercial       Até 1000          R$ 0,55
#               Acima de 1000       R$ 0,60
# Industrial      Até 5000          R$ 0,55
#               Acima de 5000       R$ 0,60

electrical_energy_use = float(input("Enter the electrical energy use in kWh: "))
type_building = input("Enter the options for type building, R for houses, I for industry and C from trades")

if type_building == 'R':
    if electrical_energy_use <= 500:
        electrical_energy_price = electrical_energy_use * 0.40
    else:
        electrical_energy_price = electrical_energy_use * 0.65
    print("The price of energy is  %.2f " % electrical_energy_price)
elif type_building == 'C':
    if electrical_energy_use <= 1000:
        electrical_energy_price = electrical_energy_use * 0.55
    else:
        electrical_energy_price = electrical_energy_use * 0.60
    print("The price of energy is  %.2f " % electrical_energy_price)
elif type_building == 'I':
    if electrical_energy_use <= 5000:
        electrical_energy_price = electrical_energy_use * 0.55
    else:
        electrical_energy_price = electrical_energy_use * 0.60
    print("The price of energy is  %.2f " % electrical_energy_price)
else:
    print("Invalid input")

# Exercício 4.13
# No programa a seguir inverta as linhas do if e else, negando a condição.
# Adicione as linhas necessárias para fazê-lo funcionar em Python.

# if a > b:
#     print("A is greater than B")
# else:
#     print("B is greater than A")

if a < b:
    print("B is greater than A")
else:
    print("A is greater than B")

# Exercício 4.14
# Reescreva o programa a seguir com if-elif-else.
# Adicione as linhas necessárias para fazê-lo funcionar em Python.

# if a < 10:
#   print("a is smaller than 10")
# if a >= 10 and a < 20:
#   print("a is greater than 10 and minor than 20")
# if a >= 20:
#   print("a is greater than 20")

if a < 10:
    print("a is smaller than 10")
elif 10 <= a < 20:
    print("a is greater than 10 and minor than 20")
if a >= 20:
    print("a is greater than 20")

# Exercício 4.15
# Reescreva o programa a seguir com if-elif-else.
# Adicione as linhas necessárias para fazê-lo funcionar em Python.

# hour = int(input("Enter the current hour: "))
# if hour < 12:
#   print("Good morning!")
# if hour >= 12 and hour < 18:
#   print("Good afternoon!")
# if hour >= 18:
#   print("Good night!")

hour = int(input("Enter the current hour: "))
if hour < 12:
    print("Good morning!")
elif 12 <= hour < 18:
    print("Good afternoon!")
else:
    print("Good night!")

# 4.16
# Corrija o programa a seguir:
# average = input("Enter your average: ")
# if average < 4:
#   print("Unfortunately you failed")
# if average < 7:
#   print("You were on the mend")
# if average > 7:
#   print("You have been approved")

average = int(input("Enter your average: "))
if average < 4:
    print("Unfortunately you failed")
elif 4 < average < 7:
    print("You were on the mend")
else:
    print("You have been approved")
