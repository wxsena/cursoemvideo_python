# Exercício Python #054 - Grupo da Maioridade
from datetime import date

ano_atual = date.today().year
maioridade = 18

pessoas = 7
pessoas_maioridade = 0
pessoas_nao_maioridade = 0

for i in range(1, pessoas + 1):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    idade = ano_atual - ano_nascimento

    if idade >= maioridade:
        pessoas_maioridade += 1
        print(f"\033[92m{i}: {idade} anos (Maioridade)\033[0m")
    else:
        pessoas_nao_maioridade += 1
        print(f"\033[91m{i}: {idade} anos (Menoridade)\033[0m")

print('=' * 30)
print(f"\033[92m{pessoas_maioridade} pessoas\033[0m atingiram a maioridade.")
print(f"\033[91m{pessoas_nao_maioridade} pessoas\033[0m ainda não atingiram a maioridade.")