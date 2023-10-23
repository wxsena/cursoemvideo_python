# Exercício Python #065 - Maior e Menor valores
soma = 0
contador = 0
maior = menor = 0

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")
        continue

    soma += numero
    contador += 1

    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.lower() != 's':
        break

if contador > 0:
    media = soma / contador
    print(f"Média: {media}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
else:
    print("Nenhum número foi digitado.")