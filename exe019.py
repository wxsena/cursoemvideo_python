# Exercício Python #019 - Sorteando um item na lista
from random import choice

aluno1 = input("Digite o nome do 1º aluno: ")
aluno2 = input("Digite o nome do 2º aluno: ")
aluno3 = input("Digite o nome do 3º aluno: ")
aluno4 = input("Digite o nome do 4º aluno: ")

escolhido = choice([aluno1, aluno2, aluno3, aluno4])

print("O aluno escolhido foi {}".format(escolhido))