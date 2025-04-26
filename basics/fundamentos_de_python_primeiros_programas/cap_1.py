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



# Exercício 5
# Modifique o programa do Projeto 4 para calcular a área de um triângulo. Emita os prompts
# apropriados para a base e a altura do triângulo, e altere os nomes das variáveis de acordo.
# Em seguida, utilize a fórmula .5 * base * height para calcular a área. Teste o programa a
# partir de uma janela IDLE.

# Exercício 6
# Escreve e teste um programa que calcula a área de um círculo. Esse programa deve solicitar
# um número representando um raio como entrada do usuário. Ele deve utilizar a fórmula
# 3.14 * radius ** 2 para calcular a área e, em seguida, produzir o resultado devidamente
# rotulado.

# Exercício 7
# Escreva e teste um programa que aceite o nome do usuário (como texto) e a idade (como um número)
# como entrada. O programa deve produzir uma sentença contendo o nome e a idade do usuário.

# Exercício 8
# Insira uma instrução de entrada utilizando a função input no prompt de shell. Quando o prompt
# solicitar a entrada, digite um número. Em seguida, tente adicionar 1 a esse número, observe
# os resultados e explique o que aconteceu.

# Exercício 9
# Insira uma instrução de entrada utilizando a função input no prompt do shell. Quando o prompt
# solicitar a entrada, digite seu primeiro nome, observe os resultados e explique o que aconteceu.

# Exercício 10
# Digite a expressão help() no prompt de shell. Siga as instruções para navegar pelos tópicos
# e módulos.