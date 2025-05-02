# Exercício 1
# Abra um shell Python, insira as seguintes expressões e observe os resultados
# a) 8
# b) 8*2
# c) 8**2
# d) 8 / 12
# e) 8 // 12
# f) 8 / 0

# Resposta:
# a) 8
# b) 16
# c) 64
# d) 0.6666666666666666
# e) 0
# f) Exception:
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# ZeroDivisionError: division by zero

# Exercício 2
# Escreva um programa em Python que imprime(exibe) seu nome, endereço e número de telefone.

name = "Teste"
address = "Avenida do teste, 123"
phone = "(12) 3456-7890"
print(f"your name is {name} your address {address} and phone {phone}")

# Exercício 3
# Avalie o seguinte código em um prompt de shell: print("Your name is", nome). Em seguida,
# atribua a name um valor apropriado e avalie a instrução novamente.

# Resposta: O comanda gera uma exception, porquee a variavel nome não foi definida
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'nome' is not defined. Did you mean: 'None'?

# Atribuindo um valor apropriado o shell executa corretamente

name = "Teste"
print("Your name is", name)

# Exercício 4
# Abra uma janela IDLE e abra o programa da figura 1-7 que calcula a área de um retângulo.
# Carregue o programa no shell pressionando a tecla F5 e corrija os erros que ocorrerem.
# Teste o programa com diferentes entradas executando-o pelo menos três vezes.

width = int(input("Enter with width: "))
height = int(input("Enter with height: "))
area = width * height
print(f"The area is {area} square units")

# Resposta:
# Teste 1 width 100 height 80 => 8000 square units
# Teste 2 width 10 height 5 => 50 square units
# Teste 3 width 32 height 25 => 800 square units

# Exercício 5
# Modifique o programa do Projeto 4 para calcular a área de um triângulo. Emita os prompts
# apropriados para a base e a altura do triângulo, e altere os nomes das variáveis de acordo.
# Em seguida, utilize a fórmula .5 * base * height para calcular a área. Teste o programa a
# partir de uma janela IDLE.

triangle_width = float(input("Enter with triangle width: "))
triangle_height = float(input("Enter with triangle height: "))
triangle_area = triangle_width * triangle_height * .5
print(f"The triangle area is {triangle_area} square units")

# Também podemos usar
# triangle_area = (triangle_width * triangle_height) / 2

# Exercício 6
# Escreve e teste um programa que calcula a área de um círculo. Esse programa deve solicitar
# um número representando um raio como entrada do usuário. Ele deve utilizar a fórmula
# 3.14 * radius ** 2 para calcular a área e, em seguida, produzir o resultado devidamente
# rotulado.
radius = float(input("Enter the radius to calcule circle area: "))
circle_area = 3.14 * (radius ** 2)
print(f"The circle area is {circle_area}")

# Exercício 7
# Escreva e teste um programa que aceite o nome do usuário (como texto) e a idade (como um número)
# como entrada. O programa deve produzir uma sentença contendo o nome e a idade do usuário.

user_name = input("Enter the user name: ")
user_age = int(input("Enter the user age: "))
print(f"The user {user_name} has {user_age} age")

# Exercício 8
# Insira uma instrução de entrada utilizando a função input no prompt de shell. Quando o prompt
# solicitar a entrada, digite um número. Em seguida, tente adicionar 1 a esse número, observe
# os resultados e explique o que aconteceu.

#number = input("Enter a number")
#number + 1
# Ocorre erro de tipagem
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# caso number seja number = int(input("Enter a number")) podemos adicionar tranquilamente um numero.

# Exercício 9
# Insira uma instrução de entrada utilizando a função input no prompt do shell. Quando o prompt
# solicitar a entrada, digite seu primeiro nome, observe os resultados e explique o que aconteceu.

name = input("Enter a name:")
# Quando digito um nome, por exemplo, "Python" ele é atribuido a variavel name, se eu digitar name é mostrado no shell
# o conteúdo do nome

# Exercício 10
# Digite a expressão help() no prompt de shell. Siga as instruções para navegar pelos tópicos
# e módulos.

# Resposta: Exibe uma central de ajuda na linha de comando, contendo links de documentação
# alguns comandos e mais...