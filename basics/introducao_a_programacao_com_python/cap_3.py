# Exercício 3.1
# Complete a tabela a seguir, marcando inteiro ou ponto flutuante
# dependendo do número  apresentado.
#
# Número    Tipo numérico
#   5         () int () float
#   5.0       () int () float
#   4.3       () int () float
#   -2        () int () float
#   100       () int () float
#   1.333     () int () float

# Resposta:
#
# Número    Tipo numérico
#   5         (x) int () float
#   5.0       () int (x) float
#   4.3       () int (x) float
#   -2        (x) int () float
#   100       (x) int () float
#   1.333     () int (x) float

# Exercício 3.2
# Complete a tabela abaixo, respondendo True ou False.
# Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.
#
#   Expressão        Resultado
#     a == c     () True () False
#     a < b      () True () False
#     d > b      () True () False
#     c! = f     () True () False
#     a == b     () True () False
#     c < d      () True () False
#     b > a      () True () False
#     c >= f     () True () False
#     f >= c     () True () False
#     c <= c     () True () False
#     c <= f     () True () False

# Resposta:
#
#   Expressão        Resultado
#     a == c     () True (x) False
#     a < b      (x) True () False
#     d > b      () True (x) False
#     c != f     () True (x) False
#     a == b     () True (x) False
#     c < d      () True (x) False
#     b > a      (x) True () False
#     c >= f     (x) True () False
#     f >= c     (x) True () False
#     c <= c     (x) True () False
#     c <= f     (x) True () False

# Exercício 3.3
# Complete a tabela a seguir utilizando a = True,
# b = False, c = True.
#
# Expressão         Resultado
#  a and a          () True () False
#  b and b          () True () False
#  not c            () True () False
#  not b            () True () False
#  not a            () True () False
#  a and b          () True () False
#  b and c          () True () False
#  a or c           () True () False
#  b or c           () True () False
#  c or a           () True () False
#  c or b           () True () False
#  c or c           () True () False
#  b or b           () True () False

# Resposta:
#
# Expressão         Resultado
#  a and a          (x) True () False
#  b and b          () True (x) False
#  not c            () True (x) False
#  not b            (x) True () False
#  not a            () True (x) False
#  a and b          () True (x) False
#  b and c          () True (x) False
#  a or c           (x) True () False
#  b or c           (x) True () False
#  c or a           (x) True () False
#  c or b           (x) True () False
#  c or c           (x) True () False
#  b or b           () True (x) False

# Exercício 3.4
# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considere que pagam imposto pessoas cujo salário é maior que
# R$ 1.200,00

# Resposta: salário > 1200

# Exercício 3.5
# Calcule o resultado da expressão A > B and C or D, utilizando
# os valores da tabela a seguir.
#
#   A     B     C     D     Resultado
#   1     2     True  False
#   10    3     False False
#   5     1     True  True

# Resposta:
#
#   A > B and C or D
#
#   A     B     C     D     Resultado
#   1     2     True  False  False
#   10    3     False False  False
#   5     1     True  True   True

# Exercício 3.6
# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está
# armazenada nas seguintes variáveis: matéria1, matéria2, matéria3.

# Resposta:
#
# materia1 > 7 and materia2 > 7 and materia3 > 7 -> True and True and True, para ser aprovado
# nesse caso avaliamos os operadores relacionais primeiro materiax > x
# depois avaliamos os operadores lógicos

# Exemplos de composição com marcadores
print("\nListagem 3.10 - Exemplo de composição com marcadores")
age = 22
print("[%d]" % age)
print("[%03d]" % age)
print("[%3d]" % age)
print("[%-3d]" % age)

# Exemplo de composição com números decimais
print("\nListagem 3.11 - Exemplo de composição com números decimais")
print("%5f" % 5)
print("%5.2f" % 5)
print("%10.5f" % 5)

# Exemplo de composição de string
print("\nListagem 3.12 - Exemplo de composição de string")
name = "João"
#age = 22
money = 51.34
print("%s tem %d anos e R$%f no bolso.\n" % (name, age, money))
print("%12s tem %3d anos e R$%5.2f no bolso.\n" % (name, age, money))
print("%12s tem %03d anos e R$%5.2f no bolso.\n" % (name, age, money))
print("%-12s tem %-3d anos e R$%-5.2f no bolso.\n" % (name, age, money))

# Fatiamento de Strings: O Fatiamento é uma funcionalidade para extrair
# partes específicas de uma string com base em critérios definidos,
# como a posição dos caracteres.

# O fatiamento funciona com a utilização de dois pontos no índice da string [0:2]
# O número à esquerda dos dois pontos indica a posição de ínicio da fatia, o da
# direita indica o fim, porém não é inclusivo

# Exemplo de fatiamento
print("\n Listagem 3.13 - Exemplo de fatiamento")
s = "ABCDEFGHI"
print(s[0:2])
print(s[1:2])
print(s[2:4])
print(s[0:5])
print(s[1:8])

# Podemos omitir o número da esquerda ou direita no fatiamento
# [:2] indica do início até o segundo caractere(exclusivo).
# [1:] indica do caractere de posição 1 até o final da string.

# Exemplo de fatiamento com omissão de valores e com índices negativos
print("\n Listagem 3.13 - Exemplo de fatiamento com omissão de valores e com índices negativos")
#s = "ABCDEFGHI"
print(s[:2])
print(s[1:])
print(s[0:-2])
print(s[:])
print(s[-1:])
print(s[-5:7])
print(s[-2:-1])

# Sequências e tempo
# Um programa é executado linha por linha pelo computador,
# executando as operações descritas no programa uma após a outra.
#
# Quando trabalhamos com variáveis, devemos lembrar que o conteúdo de
# uma variável pode mudar com o tempo.

# Exemplo de sequência e tempo
print("\n Listagem 3.15 - Exemplo de sequência e tempo")
debt = 0
buy = 100
debt = debt + buy
buy = 200
debt = debt + buy
buy = 300
debt = debt + buy
buy = 0
print(debt)

# Mudança no valor de duas variáveis no tempo
#
# Tempo  -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
# Compra        100       200       300        0
# Divida    0        100       300       600       600

# Exercício 3.7
# Faça um programa que peça dois números inteiros.
# Imprima a soma desses dois números na tela

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("The sum of numbers is: %d" % (number1 + number2))

# Exercício 3.8
# Escreva um programa que leia um valor em metros e o exiba
# convertido em milímetros

meters = float(input("Enter the meters to convert in millimeters:\n"))
millimeters = meters * 1000
print("The result of conversion of %.2f meter(s) in millimeters is %.2f" %(meters, millimeters))

# Exercício 3.9
# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total de segundos
#
# Esboço: 1m = 60s, 1h = 60m ou 3600s 1d = 24h ou 24*3600 = 86400

days = int(input("Enter the quantity of days: \n"))
hours = int(input("Enter the quantity of hours: \n"))
minutes = int(input("Enter the quantity of minutes: \n"))
seconds = int(input("Enter the quantity of seconds: \n"))

total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
print("Total in seconds: ", total_seconds)

# Exercício 3.10
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar
# o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
# e do novo salário

salary_value = float(input("Enter the salary: \n"))
percentage = int(input("Enter the percentage of salary increase: \n"))
value_increase = salary_value * percentage / 100
salary_increase = salary_value + value_increase
print("\nThe increase is : R$ %5.2f and the new salary is: R$ %5.2f" %(value_increase , salary_increase))
