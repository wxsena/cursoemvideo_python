# Exercício Python #060 - Cálculo do Fatorial
from colorama import init, Fore, Style

init(autoreset=True)

def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não definido para números negativos"
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

while True:
    try:
        print(Style.BRIGHT + Fore.MAGENTA + "Calculadora de Fatorial")
        numero = int(input("Digite um número para calcular o fatorial (ou digite 0 para sair): "))

        if numero == 0:
            print(Fore.RED + "Programa encerrado.")
            break

        resultado = calcular_fatorial(numero)

        if isinstance(resultado, int):
            print(Fore.GREEN + f"{numero}! = {resultado}")
        else:
            print(Fore.RED + resultado)
    except ValueError:
        print(Fore.RED + "Por favor, insira um número inteiro válido.")