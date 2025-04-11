# Listagem 4.2 - Condições
#
# a = int(input("Primeiro Valor: "))
# b = int(input("Segundo Valor: "))
# if a > b:
#   print("O primeiro número é o maior!")
# if b > a:
#   print("O segundo número é o maior!")

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

print("The biggest number is %d and the smaller is %d" %(bigger, smaller))

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

print("The value of increase is: %.2f" %increase)

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

print("The Ticket price is %.2f" %ticket_price)

# Uma forma outra forma de resolver:
# ticket_price = passenger_travel_distance * (0.50 if passenger_travel_distance <= 200 else 0.45)
