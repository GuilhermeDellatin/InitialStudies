# Exercício 2.1
# Converta as expressões matemáticas para que possam ser calculadas
# usando o interpretador Python.
#
# 10 + 20 x 30
# 4² + 30
#(9^4 + 2) x 6 - 1

#1 - Resposta: Para a expressão 10 + 20 * 30 = 610
#2 - Resposta: Para a expressão 4 ** 2 + 30 = 46
#3 - Resposta: Para a expressão (9 ** 4 + 2) * 6 - 1 = 39377

# Exercício 2.2
# Digite a seguinte expressão no interpretador:
#
# 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
#
# Tente resolver o mesmo cálculo, usando lápis e papel.
# Observe como a prioridade das operações é importante.

# Resposta: Para a expresão 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2 = 81.0

# Exercício 2.3
# Faça um programa que exiba seu nome na tela.

print("Guilherme Fernandes Dellatin")

# Exercício 2.4
# Escreva um programa que exiba o resultado de 2a x 3b
# onde a vale 3 e b vale 5.
a = 3
b = 5
result = (2 * a) * (3 * b)
print(result)

# Exercício 2.5
# Modifique o primeiro programa, listagem 2.7, de forma a calcular
# a soma de três variáveis.
#
# a = 2
# b = 3
# print(a + b)
number1 = 2
number2 = 3
number3 = 4
result_sum_numbers = number1 + number2 + number3
print(result_sum_numbers)

# Exercício 2.6
# Modifique o programa da listagem 2.11, de forma que ele calcule um aumento de 15%
# para um salário de R$ 750.
#
# 2.11
# salary = 1500
# increase = 5
# print(salary + (salary * increase / 100))
salary = 750
increase = 15
print(salary + (salary * increase / 100))