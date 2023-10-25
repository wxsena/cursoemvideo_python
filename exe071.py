# Exercício Python #071 - Simulador de Caixa Eletrônico
from termcolor import colored

def sacar_dinheiro(valor_saque):
    cedulas = [50, 20, 10, 1]
    resultado = {}

    for cedula in cedulas:
        if valor_saque >= cedula:
            quantidade_cedulas = valor_saque // cedula
            resultado[cedula] = quantidade_cedulas
            valor_saque %= cedula

    return resultado

def exibir_cedulas(saque):
    print(colored("\nCédulas a serem entregues:", "cyan"))
    for cedula, quantidade in saque.items():
        print(colored(f"R${cedula}: {quantidade} cédula(s)", "green"))

while True:
    try:
        valor_saque = int(input(colored("Digite o valor a ser sacado (ou 0 para sair): R$ ", "yellow")))
        if valor_saque == 0:
            break
        if valor_saque < 0:
            print(colored("Valor inválido. Insira um valor positivo.", "red"))
            continue

        saque = sacar_dinheiro(valor_saque)
        exibir_cedulas(saque)
    except ValueError:
        print(colored("Entrada inválida. Insira um valor numérico.", "red"))

print(colored("Obrigado por usar nosso caixa eletrônico. Volte sempre!", "magenta"))