# Programa 6.1 Calculo da media
#
#notas = [6, 7, 5, 8, 9]
#soma = 0
#x = 0
#while x < 5:
#    soma += notas[x]
#    x += 1
#print(f"Média: {soma / x:5.2f}")

# Programa 6.2 Calculo da media com notas digitadas
#
#notas = [0, 0, 0, 0, 0]
#soma = 0
#x = 0
#while x < 5:
#    notas[x] = int(input(f"Nota {x}: "))
#    soma += notas[x]
#    x += 1
#x = 0
#while x < 5:
#    print(f"Nota {x}: {notas[x]:6.2f}")
#    x += 1
#print(f"Media: {soma / x:5.2f}")

# Exercício 6.1
# Modifique o Programa 6.2 para ler 7 notas em vez de 5.

grades = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
sum_grades = 0
grade = 0

while grade < 7:
    grades[grade] = float(input(f"Grade {grade}: "))
    sum_grades += grades[grade]
    grade += 1

grade = 0

while grade < 7:
    print(f"Grade {grade}: {grades[grade]:6.2f}")
    grade += 1

print(f"Average: {sum_grades / grade:5.2f}")