# Exercício Python #033 - Maior e menor valores
try:
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))
    c = int(input("Terceiro valor: "))
except ValueError:
    print("Por favor, insira apenas valores inteiros.")
    exit()

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))