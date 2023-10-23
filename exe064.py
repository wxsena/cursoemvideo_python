# Exercício Python #064 - Tratando vários valores v1.0
soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (999 para parar): "))

    if numero == 999:
        break

    soma += numero
    contador += 1

print(f"Você digitou {contador} números.")
print(f"A soma dos números é: {soma}")