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