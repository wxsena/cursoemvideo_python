# Exercício Python #015 - Aluguel de Carros
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos quilômetros foram percorridos? "))

if dias > 0 and km > 0:
    pago = (dias * 60) + (km * 0.15)
    print("O valor a ser pago é de R$ {:.2f}".format(round(pago, 2)))
else:
    print("Valores inválidos fornecidos.")