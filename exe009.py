# Exercício Python #009 - Tabuada
ni = int(input("Digite um número qualquer: "))
for i in range(1, 11):
    resultado = ni * i
    linha = f"{ni} x {i:02} = {resultado}"
    print(linha)