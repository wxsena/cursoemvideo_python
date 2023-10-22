# Exercício Python #049 - Tabuada v.2.0
numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
