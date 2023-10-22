# Exercício Python #036 - Aprovando Empréstimo
valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
anos_financiamento = int(input('Quantos anos de financiamento? '))

prestacao = valor_casa / (anos_financiamento * 12)
limite_prestacao = salario_comprador * 30 / 100

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_financiamento} anos,', end=' ')
print(f'a prestação será de R${prestacao:.2f}')

if prestacao <= limite_prestacao:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')