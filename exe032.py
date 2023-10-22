# Exercício Python #032 - Ano Bissexto
from datetime import date

try:
    ano = int(input("Digite o ano que você quer analisar (coloque 0 para analisar o ano atual): "))
    
    if ano == 0:
        ano = date.today().year

    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print("O ano {} é bissexto.".format(ano))
    else:
        print("O ano {} não é bissexto.".format(ano))
except ValueError:
    print("Por favor, insira um ano válido (número inteiro).")