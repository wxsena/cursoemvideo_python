# Exercício Python #044 - Gerenciador de Pagamentos
import time

preco_produto = float(input('Informe o preço do produto: R$ '))
forma_pagamento = int(input('''Escolha a forma de pagamento:
[ 1 ] - À vista dinheiro/cheque
[ 2 ] - À vista no cartão
[ 3 ] - Em até 2x no cartão
[ 4 ] - 3x ou mais no cartão
Digite o número da opção desejada: '''))

print('Calculando o valor a ser pago...')
time.sleep(2)

if forma_pagamento == 1:
    desconto = 0.10
    descricao_pagamento = 'à vista dinheiro/cheque'
elif forma_pagamento == 2:
    desconto = 0.05
    descricao_pagamento = 'à vista no cartão'
elif forma_pagamento == 3:
    desconto = 0
    descricao_pagamento = 'em até 2x no cartão'
elif forma_pagamento == 4:
    desconto = 0.20
    descricao_pagamento = '3x ou mais no cartão'
else:
    desconto = 0
    descricao_pagamento = 'opção de pagamento inválida'

valor_a_pagar = preco_produto - (preco_produto * desconto)

print(f'Preço do produto: R$ {preco_produto:.2f}')
print(f'Forma de pagamento: {descricao_pagamento}')
print(f'Desconto aplicado: {desconto * 100}%')

time.sleep(2)

print(f'Valor a ser pago: R$ {valor_a_pagar:.2f}')