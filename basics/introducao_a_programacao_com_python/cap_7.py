# Algumas operações com Strings

# Podemos acessar strings como listas, e strings são imutáveis, e se quisermos trabalhar caractere a caractere
# com uma string, alterando os seus valores, podemos transformá-la numa lista:

# L = list("Alô mundo") -> transforma cada caractere da string num elemento da lista
# L[0] = "a"
# print(L) -> ['a', 'l', 'ô', 'm', 'u', 'n', 'd', o']
# s = "".join(L) -> join transforma uma lista em string
# print(s) -> alô Mundo

# .startswith("") -> verifica os primeiros caracteres da string
# .endswith("") -> verifica os últimos caracteres da string
# .lower() -> retorna uma cópia da string com os caracteres minúsculos
# .upper() -> retorna uma cópia da string com os caracteres maiúsculos
# s = "Maria Amélia Souza"
# Amélia in s -> True, Amélia not in s -> False, podemos usar o operador in e not in para verificar
# se uma palavra pertence a uma string.
# count() -> Conta recorrências de uma letra ou palavra na string
# find("") -> Pesquisa se uma string está dentro de outra(dir -> esq)
# rfind("") -> Pesquisa se uma string está dentro de outra(esq -> dir) busca reversa*
# s[7:] -> Fatiamento, retorna a string a partir de determinada posição [inicio, fim]
# index() -> Retorna o index da substring ou uma exception do tipo ValueError
# rindex() -> Retorna o index(esq -> dir) da substring ou uma exception do tipo ValueError

# Programa 7.1 Pesquisa de todas as ocorrências
"""
s = "um tigre, dois tigres, três tigres"
p = 0

while p > -1:
    p = s.find("tigre", p)
    if p >= 0:
        print(f"Posição: {p}")
        p += 1
"""

# Exercício 7.1
# Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima
# a posição de início.
# 1.ª string: AABBEFAATT
# 2.ª string: BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT

first_string = "AABBEFAATT"
second_string = "BE"
occurrence = second_string in first_string
if occurrence:
    print(f"{second_string} find in {first_string.find(second_string)} of {first_string} using find method")
    print(f"{second_string} find in {first_string.index(second_string)} of {first_string} using index method")

# Exercício 7.2
# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
# 1.ª string: AAACTBF
# 2.ª string: CBT
# Resultado: CBT A ordem dos caracteres da string gerada não é importante,
# mas deve conter todas as letras comuns a ambas.

# Exercício 7.3
# Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem
# em uma delas.
# 1.ª string: CTA
# 2.ª string: ABC
# 3.ª string: BT
# A ordem dos caracteres da terceira string não é importante.

# Exercício 7.4
# Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
# String: TTAAC Resultado: T: 2x A: 2x C: 1x

# Exercício 7.5
# Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram
# retirados da primeira.
# 1.ª string: AATTGGAA
# 2.ª string: TG
# 3.ª string: AAAA

# Exercício 7.6
# Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos
# caracteres da segunda pelos da terceira.
# 1.ª string: AATTCGAA
# 2.ª string: TG
# 3.ª string: AC Resultado:
# AAAACCAA

# Exercício 7.7
# Escreva um programa que peça ao usuário que digite uma frase e imprima quantas vogais ela contém.
# Não considere maiúsculas e minúsculas como diferentes. Exemplo: uma frase como “A casa” deve
# imprimir três “as”.