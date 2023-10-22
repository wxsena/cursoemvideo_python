# Exercício Python #027 - Primeiro e último nome de uma pessoa
n = input("Digite seu nome completo: ").strip()
nome = n.split()
tamanho_nome = len(nome)
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[tamanho_nome-1]))