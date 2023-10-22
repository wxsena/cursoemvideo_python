# Exercício Python #048 - Soma ímpares múltiplos de três
soma = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero

print("A soma dos múltiplos de três e ímpares no intervalo de 1 a 500 é:", soma)