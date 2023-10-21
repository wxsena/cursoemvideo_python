# Exercício Python #010 - Conversor de Moedas
while True:
    try:
        reais = float(input("Quantos reais você possui na carteira? "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

conversao = reais / 5
print("Com R$ {:.0f}, você pode comprar aproximadamente US$ {:.0f}!".format(reais, conversao))