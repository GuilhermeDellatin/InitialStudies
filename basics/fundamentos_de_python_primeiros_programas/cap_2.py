# Exercício 1
# Seja a variável x definida com valor "dog" e y com valor "cat".
# Escreva os valores retornados pelas seguintes operações:

# a. x + y
# b. "the " + x + " loves the " + y
# c. x * 4

# Resposta:
# a. 'dogcat'
# b. 'the dog loves the cat'
# c. 'dogdogdogdog'

# Exercício 2
# Escreva uma string que contenha o seu nome e endereço em linhas separadas
# utilizando caracteres de nova linha incorporado. Em seguida, escreva
# o mesmo literal de string sem os caracteres de nova linha.

info = "Guilherme \nRua da computação, 0101 \nPython - 1010"
print(info)

info_without_new_line = "Guilherme Rua da computação, 0101 Python - 1010"
print(info_without_new_line)

# Exercício 3
# Como incluir um apóstrofo como um caractere num literal de string?

# Resposta:
# Dentro de "" aspas duplas o apóstrofo ' vai funcionar normalmente
# Se a string tiver '' aspas simples o apóstrofo ' precisa de uma \ para funcionar

apostrofe = "It's a beautiful day"
print(apostrofe)

other_apostrofe = 'It\'s a beautiful day'
print(other_apostrofe)

# Exercício 4
# O que acontece quando a função print imprime um literal de string com
# caracteres de nova linha incorporados?

# Resposta:
# O caractere é interpretado como uma quebra de linha e a função print
# vai exibir múltiplas linhas automaticamente

# Exercício 5
# Quais dos seguintes nomes de variáveis são válidos?
# a. length
# b. _width
# c. firstBase
# d. 2MoreToGo
# e. halt!

# Resposta: Os nomes de variáveis válidos são a. length, b. _width e c. firstBase

# Exercício 6
# Liste dois dos propósitos da documentação do programa.

# Resposta:
# Escrever uma breve instrução da finalidade de um programa
# Facilitar o entendimento de um código que tem uma certa complexidade para outros

# Exercício 7
# Seja x = 8 e y = 2. Escreva os valores das seguintes expressões:
# a. x + y * 3
# b. (x + y) * 3
# c. x ** y
# d. x % y
# e. x / 12.0
# f. x // 6

# Resposta:
# a. 14
# b. 30
# c. 64
# d. 0
# e. 0.6666666666666666
# f. 1

x = 8
y = 2

print(x + y * 3)
print((x + y) * 3)
print(x ** y)
print(x % y)
print(x / 12.0)
print(x // 6)

# Exercício 8
# Seja x = 4.66 Escreva os valores das seguintes expressões:
# a. round(x)
# b. int(x)

# Resposta:
# a. 5
# b. 4

x = 4.66
print(round(x))
print(int(x))

# Exercício 9
# Como um programador Python arredonda um valor float para o valor int mais próximo?

# Resposta:
# Em Python para arredondar um valor float para o inteiro mais próximo usamos a função round()

# Exercício 10
# Como um programador Python concatena um valor numérico a um valor de string?

# Resposta:
# Em Python para concatenar um valor numérico a uma string primeiro precisamos converter o valor numérico em string.
# Também podemos fazer de uma forma mais moderna e recomendada que é usando f-strings

# Exercício 11
# Suponha que a variável x tenha o valor 55. Utilize uma instrução de atribuição para
# incrementar o valor de x por 1.