# Exercício Python #037 - Conversor de Bases Numéricas
num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    binario = bin(num)[2:]
    print('{} convertido para BINÁRIO é igual a {}'.format(num, binario))
elif opcao == 2:
    octal = oct(num)[2:]
    print('{} convertido para OCTAL é igual a {}'.format(num, octal))
elif opcao == 3:
    hexadecimal = hex(num)[2:]
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hexadecimal))
else:
    print('Opção inválida. Tente novamente.')