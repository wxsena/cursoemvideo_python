# Exercício Python #007 - Média Aritmética
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    try:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
        break
    except ValueError:
        print("Digite um valor válido.")
        tentativas += 1

if tentativas == max_tentativas:
    print("Número máximo de tentativas excedido.")
else:
    ma = sum([n1, n2]) / 2
    print('A média aritmética entre {} e {} é {}'.format(n1, n2 , ma))