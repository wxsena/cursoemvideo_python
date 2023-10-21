# Exercício Python #012 - Calculando Descontos
prod = float(input("Qual é o preço do produto? "))
desc = prod - (prod * 25/100)
print("Com o desconto, o produto que custava R$ {:.2f} agora está disponível por R$ {:.2f}".format(prod, desc))