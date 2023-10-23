# Exercício Python #061 - Progressão Aritmética v2.0
from colorama import init, Fore, Style

init(autoreset=True)

print(Style.BRIGHT + Fore.MAGENTA + "Calculadora de Progressão Aritmética (PA)")
print("=" * 40)

primeiro_termo = int(input(Fore.CYAN + "Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
quantidade_termos = int(input("Digite a quantidade de termos a serem exibidos: "))

termo = primeiro_termo
cont = 1

print(Fore.GREEN + "Progressão Aritmética:")
while cont <= quantidade_termos:
    print(f"Termo {cont:2}: {termo}")
    termo += razao
    cont += 1