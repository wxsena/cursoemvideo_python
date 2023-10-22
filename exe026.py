# Exercício Python #026 - Primeira e última ocorrência de uma string
frase = input("Digite uma frase: ")
frase = frase.lower()

count_a = frase.count("a")
print("A letra A aparece {} vezes na frase.".format(count_a))

first_a = frase.find("a") + 1
print("A primeira letra A apareceu na posição {}".format(first_a))

last_a = frase.rfind("a") + 1
print("A última letra A apareceu na posição {}".format(last_a))