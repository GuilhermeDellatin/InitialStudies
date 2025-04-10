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