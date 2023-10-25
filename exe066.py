# Exercício Python #066 - Vários números com flag
soma = 0
contador = 0

while True:
    try:
        numero = int(input("Digite um número inteiro (ou 999 para parar): "))
        if numero == 999:
            break
        soma += numero
        contador += 1
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print(f"Foram digitados {contador} números.")
print(f"A soma dos números é: {soma}")