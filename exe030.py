# Exercício Python #030 - Par ou Ímpar?
numero = input("Digite um número inteiro: ")
if numero.isdigit():
    numero = int(numero)
    if numero & 1 == 0:
        print("O número " + str(numero) + " é PAR")
    else:
        print("O número " + str(numero) + " é ÍMPAR")
else:
    print("Entrada inválida. Por favor, digite um número inteiro.")