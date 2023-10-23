# Exercício Python #059 - Criando um Menu de Opções
import time
from colorama import init, Fore, Style

init(autoreset=True)

def somar(val1, val2):
    return val1 + val2

def multiplicar(val1, val2):
    return val1 * val2

def subtrair(val1, val2):
    return val1 - val2

def dividir(val1, val2):
    if val2 != 0:
        return val1 / val2
    else:
        return None

def calcular_maior(val1, val2):
    return max(val1, val2)

def elevar_a_potencia(val1, val2):
    return val1 ** val2

while True:
    try:
        print(Style.BRIGHT + Fore.BLUE + "Menu de opções:")
        print("[ 1 ] " + Fore.CYAN + "Somar")
        print("[ 2 ] " + Fore.CYAN + "Multiplicar")
        print("[ 3 ] " + Fore.CYAN + "Subtrair")
        print("[ 4 ] " + Fore.CYAN + "Dividir")
        print("[ 5 ] " + Fore.CYAN + "Maior")
        print("[ 6 ] " + Fore.CYAN + "Elevar à Potência")
        print("[ 7 ] " + Fore.CYAN + "Sair do programa")

        opcao = int(input(Fore.BLUE + "Escolha uma opção: "))

        if opcao in range(1, 7):
            valor1 = float(input(Fore.MAGENTA + "Digite o primeiro valor: "))
            valor2 = float(input(Fore.MAGENTA + "Digite o segundo valor: "))

        if opcao == 1:
            resultado = somar(valor1, valor2)
            print(Fore.GREEN + f"A soma de {valor1} e {valor2} é igual a {resultado}")
        elif opcao == 2:
            resultado = multiplicar(valor1, valor2)
            print(Fore.GREEN + f"A multiplicação de {valor1} e {valor2} é igual a {resultado}")
        elif opcao == 3:
            resultado = subtrair(valor1, valor2)
            print(Fore.GREEN + f"A subtração de {valor1} por {valor2} é igual a {resultado}")
        elif opcao == 4:
            resultado = dividir(valor1, valor2)
            if resultado is not None:
                print(Fore.GREEN + f"A divisão de {valor1} por {valor2} é igual a {resultado}")
            else:
                print(Fore.RED + "Não é possível dividir por zero.")
        elif opcao == 5:
            resultado = calcular_maior(valor1, valor2)
            print(Fore.GREEN + f"O maior valor entre {valor1} e {valor2} é {resultado}")
        elif opcao == 6:
            resultado = elevar_a_potencia(valor1, valor2)
            print(Fore.GREEN + f"{valor1} elevado à potência {valor2} é igual a {resultado}")
        elif opcao == 7:
            print(Fore.BLUE + "Programa encerrado.")
            break
        else:
            print(Fore.RED + "Opção inválida. Por favor, escolha uma opção válida.")

        time.sleep(2)
    except ValueError:
        print(Fore.RED + "Por favor, insira números válidos.")