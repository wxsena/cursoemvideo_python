# Exercício Python #035 - Analisando Triângulo v1.0
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Os lados do triângulo devem ter valores maiores que zero.")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Não é possível formar um triângulo com esses lados.")
else:
    print("É possível formar um triângulo com os lados informados.")