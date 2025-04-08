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

