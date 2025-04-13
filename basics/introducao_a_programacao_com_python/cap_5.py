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