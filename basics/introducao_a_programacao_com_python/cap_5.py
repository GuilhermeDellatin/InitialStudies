# while <condição>:
#   block
#
# Exemplo:
# x = 1
# while x <= 3:
#   print(x)
#   x = x + 1

# Exercício 5.1
# Modifique o programa para exibir os números de 1 a 100.

x = 1
while x <= 100:
    print(x)
    x = x + 1

# Exercício 5.2
# Modifique o programa para exibir os números de 50 a 100.

x = 50
while x <= 100:
    print(x)
    x = x + 1

# Exercício 5.3
# Faça um programa para escrever a contagem regressiva do lançamento
# de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown = countdown - 1

print("Fire!")

# Exemplos
#
# fim = int(input("Digite o último número a imprimir:"))
# x = 0
# while x <= fim:
#   if x % 2 == 0:
#       print(x)
#   x = x + 1
#
# fim = int(input("Digite o último número a imprimir:"))
# x = 0
# while x <= fim:
#   print(x)
#   x = x + 2

# Exercício 5.4
# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas,
# dessa vez, apenas os números ímpares.

end = int(input("Enter the last number to print: "))
number = 1
while number <= end:
    if number % 2 != 0:
        print(number)
    number = number + 1

end = int(input("Enter the last number to print: "))
number = 1
while number <= end:
    print(number)
    number = number + 2

# Exercício 5.5
# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

number = 0
while number < 30:
    if number  % 3  == 0:
        print(number)
    number = number + 1

number = 0
while number < 30:
    print(number)
    number = number + 3

# Exemplos tabuada de adição
#
# n = int(input("Tabuada de:"))
# x = 1
# while x <= 10:
#   print(n + x)
#   x = x + 1

# Exercício 5.6
# Altere o programa anterior para exibir os resultados no mesmo formato
# de uma tabuada de multiplicação: 2x1 = 2, 2x2 = 4,....

number = int(input("Multiplication table:"))
multiply = 1
while multiply <= 10:
    print(number * multiply)
    multiply = multiply + 1

# Exercício 5.7
# Modifique o programa anterior de forma que o usuário também digite o início
# e o fim da tabuada, em vez de começar com 1 e 10.

number = int(input("Multiplication table:"))
number_init = int(input("Enter the init number:"))
number_end = int(input("Enter the end number:"))
while number_init <= number_end:
    print(number * number_init)
    number_init = number_init + 1

# Exercício 5.8
# Escreva um programa que leia dois números. Imprima o resultado da multiplicação
# do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para
# calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números
# como somas sucessivas de um deles. Assim, 4x5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

number_one = int(input("Enter the number one:"))
number_two = int(input("Enter the number two:"))

result = 0
count = 1
while count <= number_one:
    result = result + number_two
    print(number_two)
    count = count + 1
print("The result of multiply is {result} with successive sum of {number_two} by {number_one} times"
      .format(result = result, number_two = number_two, number_one = number_one))

result = 0
count = 1
while count <= number_two:
    result = result + number_one
    print(number_one)
    count = count + 1
print("The result of multiply is {result} with successive sum of {number_one} by {number_two} times"
      .format(result = result, number_one = number_one, number_two = number_two))

# Exercício 5.9
# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro
# pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma
# e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente
# da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

number_one = int(input("Enter the number one:"))
number_two = int(input("Enter the number two:"))
quotient = 0

if number_two == 0:
    print("Division by 0  is not permitted")
else:
    while number_one >= number_two:
        number_one = number_one - number_two
        quotient = quotient + 1
        print(number_two)
rest = number_one


print("The result of division is {quotient} with rest {rest}, successive sub of {number_two} by {quotient} times"
      .format(number_two = number_two, rest = rest, quotient = quotient))

# Exemplo
#
#pontos = 0
#questao = 1
#while questao <= 3:
#    resposta = input(f"Resposta da questão {questao}: ")
#    if questao == 1 and resposta == "b":
#        pontos = pontos + 1
#    if questao == 2 and resposta == "a":
#        pontos = pontos + 1
#    if questao == 3 and resposta == "d":
#        pontos = pontos + 1
#    questao = questao + 1
#print(f"O aluno fez {pontos} pontos(s)")

# Exercício 5.10
# Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas
# em todas as questões.

points = 0
question = 1
while question <= 3:
    answer = input("f Answer of question {question}: ")
    if question == 1 and answer == 'b' or answer ==  'B':
        points += 1
    if question == 2 and answer == 'a' or answer ==  'A':
        points += 1
    if question == 3 and answer == 'd' or answer ==  'D':
        points += 1
    question += 1
print(f"The student make {points} point(s)")

# Exercício 5.11
# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores
# mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

initial_deposit = float(input("Enter the initial value of deposit: "))
interest_rate = float(input("Enter the interest rate of investment 0.1 to 10%: "))
month = 1
balance = initial_deposit

while month <= 24:
    balance += balance * interest_rate
    print(f"Monthly {month} value: R$ {balance:.2f}")
    month += 1
print(f"Total gained with interest rate R$ {balance:.2f}")

# Exercício 5.12
# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será
# depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

initial_deposit = float(input("Enter the initial value of deposit: "))
interest_rate = float(input("Enter the interest rate of investment 0.1 to 10%: "))
month_deposit = float(input("Enter the monthly deposit: "))
month = 1
balance = initial_deposit

while month <= 24:
    balance += balance * interest_rate + month_deposit
    print(f"Monthly {month} value: R$ {balance:.2f}")
    month += 1
print(f"Total gained with interest rate R$ {balance:.2f}")