# Exercício Python #050 - Soma dos pares
soma = 0

for i in range(1, 7):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    if numero % 2 == 0:
        soma += numero

print(f"A soma dos números pares é: {soma}")