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

# Exercício 5.13
# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o
# valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total
# de juros pago.

initial_debt = float(input("Enter the initial value of a debt: "))
interest_debt = float(input("Enter the debt interest ex 10 for 10% "))
month_debt_payment = float(input("Enter the monthly payment of debit: "))
debt = initial_debt
month = 1
interest_pay = 0

while debt > month_debt_payment:
    interest = debt  * interest_debt / 100
    debt = debt + interest - month_debt_payment
    interest_pay = interest_pay + interest
    print(f"Debt balance for the month {month} is R${debt:.2f}.")
    month += 1

print(f"To pay a debit you need R${initial_debt:.2f}, and {interest_debt:.2f} % of initial debt,")
print(f"You need {month - 1} months, pay a total interest R${interest_pay:.2f} of interest pay.")
print(f"In last month, you have a R${debt:.2f} to pay.")

# Exercício 5.14
# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o
# usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a
# soma e a média aritmética.

input_number = int(input("Enter number to calcule average, enter 0 to stop program: "))
quantity_numbers = 0
sum_numbers = 0

while input_number != 0:
    quantity_numbers += 1
    sum_numbers += input_number
    input_number = int(input("Enter number to calcule average, enter 0 to stop program: "))

average = sum_numbers / quantity_numbers

print(f"Quantity of entered numbers is {quantity_numbers} "
      f"and sum of number is {sum_numbers} "
      f"and your average is {average}")

# Exercício 5.15
# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário
# que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o
# preço de cada produto:
#
# Código Preço
# 1      0,50
# 2      1,00
# 3      4,00
# 5      7,00
# 9      8,00
#
# Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve
# gerar a mensagem de erro “Código inválido”.

total_price = 0
total_quantity = 0

while True:
    product_code = int(input("Enter the code of product the code is 1, 2, 3, 5, 9 or 0 for break: "))
    if product_code == 0:
        break
    elif product_code != 1 and product_code != 2 and product_code != 3 and product_code != 5 and product_code != 9:
        print("Invalid code.")
    else:
        item_quantity = int(input("Enter the quantity of product to buy: "))
        if product_code == 1:
            total_price += 0.5 * item_quantity
            total_quantity += item_quantity
        elif product_code == 2:
            total_price += 1.0 * item_quantity
            total_quantity += item_quantity
        elif product_code == 3:
            total_price += 4.0 * item_quantity
            total_quantity += item_quantity
        elif product_code == 5:
            total_price += 7.0 * item_quantity
            total_quantity += item_quantity
        else:
            total_price += 8.0 * item_quantity
            total_quantity += item_quantity

print(f"Total price of product buying is {total_price:.2f} and the quantity of item buying is {total_quantity}")

# Programa 5.1 Contagem de cédulas
#
#valor = int(input("Digite o valor a pagar: "))
#cedulas = 0
#atual = 50
#apagar = valor
#
#while True:
#    if atual <= apagar:
#        apagar -= atual
#        cedulas += 1
#    else:
#        print(f"{cedulas} cedula(s) de R${atual}")
#        if apagar == 0:
#            break
#        if atual == 50:
#            atual = 20
#        elif atual == 20:
#            atual = 10
#        elif atual == 10:
#            atual = 5
#        elif atual == 5:
#            atual = 1
#        cedulas = 0

# Exercício 5.16
# Execute o Programa 5.1 para os seguintes valores: 501, 745, 384, 2, 7 e 1.
#
# Resposta: Programa executado para cada valor, o retorno é correto

# Exercício 05.17
# O que acontece se digitarmos 0 (zero) no valor a pagar?
#
# Resposta: Ele exibirá 0 cédula(s) de R$50

# Exercício 05.18
# Modifique o programa para também trabalhar com notas de R$ 100.

value = int(input("Enter the value to pay: "))
cedulas = 0
actual = 100
to_pay = value

while True:
    if actual <= to_pay:
        to_pay -= actual
        cedulas += 1
    else:
        print(f"{cedulas} cedula(s) de R${actual}")
        if to_pay == 0:
            break
        if actual == 100:
            actual = 50
        elif actual == 50:
            actual = 20
        elif actual == 20:
            actual = 10
        elif actual == 10:
            actual = 5
        elif actual == 5:
            actual = 1
        cedulas = 0

# Exercício 05.19
# Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05,
# 0,10 e 0,50

value = float(input("Enter the value to pay: "))
cedulas = 0
actual = 100
to_pay = value

while True:
    if actual <= to_pay:
        to_pay -= actual
        cedulas += 1
    else:
        print(f"{cedulas} cedula(s) de R${actual}")
        if to_pay < 0.01:
            break
        if actual == 100:
            actual = 50
        elif actual == 50:
            actual = 20
        elif actual == 20:
            actual = 10
        elif actual == 10:
            actual = 5
        elif actual == 5:
            actual = 1
        elif actual == 1:
            actual = 0.50
        elif actual == 0.50:
            actual = 0.10
        elif actual == 0.10:
            actual = 0.05
        elif actual == 0.05:
            actual = 0.02
        elif actual == 0.02:
            actual = 0.01
        cedulas = 0

# Exercício 05.20
# O que acontece se digitarmos 0,001 no programa anterior? Caso ele não funcione, altere-o de forma a
# corrigir o problema.

value = float(input("Enter the value to pay: "))
cedulas = 0
actual = 100
to_pay = value

while True:
    if actual <= to_pay:
        to_pay -= actual
        cedulas += 1
    else:
        print(f"{cedulas} cedula(s) de R${actual}")
        if to_pay < 0.001:
            break
        if actual == 100:
            actual = 50
        elif actual == 50:
            actual = 20
        elif actual == 20:
            actual = 10
        elif actual == 10:
            actual = 5
        elif actual == 5:
            actual = 1
        elif actual == 1:
            actual = 0.50
        elif actual == 0.50:
            actual = 0.10
        elif actual == 0.10:
            actual = 0.05
        elif actual == 0.05:
            actual = 0.02
        elif actual == 0.02:
            actual = 0.01
        elif actual == 0.01:
            actual = 0.001
        cedulas = 0

# Exercício 05.21
# Reescreva o Programa 5.1 de forma a continuar executando até que o valor digitado seja 0.
# Utilize repetições aninhadas.

value = int(input("Enter the value to pay or zero to exit: "))

while value != 0:
    cedulas = 0
    actual = 50
    to_pay = value

    while True:
        if actual <= to_pay:
            to_pay -= actual
            cedulas += 1
        else:
            print(f"{cedulas} cedula(s) de R${actual}")
            if to_pay == 0:
                break
            if actual == 50:
                actual = 20
            elif actual == 20:
                actual = 10
            elif actual == 10:
                actual = 5
            elif actual == 5:
                actual = 1
            cedulas = 0

    value = int(input("Enter the value to pay or zero to exit: "))

# Programa 5.2 Tabuada com repetições aninhadas
#
#tabuada = 1
#while tabuada <= 10:
#    numero = 1
#    while numero <= 10:
#        print(f"{tabuada} x {numero} = {tabuada * numero}")
#        numero += 1
#    tabuada += 1

# Exercício 05.22
# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação
# e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

operation = input("Enter the operations: * / + - or x to exit")

while operation != 'x':
    table = 1

    if (operation != '*' and operation != '/' and operation != '+'
            and operation != '-' and operation != 'x'):
        print("Invalid operation")
    else :
        while table <= 10:
            number = 1
            while number <= 10:
                if operation == '*':
                    print(f"{table} x {number} = {table * number}")
                    number += 1
                elif operation == '/':
                    print(f"{table} / {number} = {table / number}")
                    number += 1
                elif operation == '+':
                    print(f"{table} + {number} = {table + number}")
                    number += 1
                elif operation == '-':
                    print(f"{table} - {number} = {table - number}")
                    number += 1
            table += 1

    operation = input("Enter the new operation: * / + - or 0 to exit")

# Exercício 05.23
# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e
# depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

number = int(input("Enter a number to verify if is prime: "))
count = 1
is_divisor_count = 0

if number < 2:
    print(f"The number {number} is not prime")
elif number == 2:
    print(f"The number {number} is prime")
else:
    while count <= number:
        if number % count != 0:
            is_divisor_count += 0
        else:
            is_divisor_count += 1
        count += 1
    if is_divisor_count == 2:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")

# Versão melhor do código
number = int(input("Enter a number to verify if is prime: "))

if number < 2:
    print(f"The number {number} is not prime")
else:
    is_prime = True
    count = 2
    while count < number:
        if number % count == 0:
            is_prime = False
            break
        count += 1
    if is_prime:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")

# Exercício 05.24
# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

prime = int(input("Enter a number to discover the primes until number: "))
count = 0
number  = 2

while count < prime:
    is_prime = True
    divider = 2

    while divider * divider <= number:
        if number  % divider == 0:
            is_prime = False
            break
        divider += 1

    if is_prime:
        print(f"The number {number} is prime")
        count += 1

    number += 1

# Exercício 05.25
# Escreva um programa que calcule a raiz quadrada de um número. Utilize o metodo de Newton para obter
# um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b=2. Calcule p
# usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p
# usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que
# 0,0001.

number = float(input("Enter a number to find your square root:"))
base = 2
p = 0

while abs(number - (base * base)) > 0.0001:
    p = (base + (number / base)) / 2
    base = p
print(f"The square root {number} is approximately {p:.4f}")

# Exercício 05.26
# Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as
# operações de soma e subtração para calcular o resultado.

number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
quotient = 0
number_aux = number_one

while number_aux >= number_two:
    number_aux -= number_two
    quotient += 1
rest = number_aux
print(f"The rest of division {number_one} / {number_two} is {rest}")

# Exercício 05.27
# Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o
# mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501

palindrome_number = int(input("Enter a number to verify if he is palindrome: "))
reverse_number = 0
aux_number = palindrome_number

while aux_number != 0:
    reverse_number = (aux_number % 10) + reverse_number * 10
    aux_number //= 10
    print(f"Reverse process: {reverse_number}, {aux_number}")

if reverse_number == palindrome_number:
    print(f"The number {palindrome_number} is palindrome and your reverse is {reverse_number}")
else:
    print(f"The number {palindrome_number} is not palindrome and your reverse is {reverse_number}")