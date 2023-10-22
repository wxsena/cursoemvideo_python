# Exercício Python #055 - Maior e menor da sequência
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def ler_peso():
    while True:
        try:
            return float(input(Fore.YELLOW + "Digite o peso: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Valor inválido. Por favor, insira um número válido para o peso." + Style.RESET_ALL)

def main():
    maior_peso = float('-inf')
    menor_peso = float('inf')
    pessoas = []

    print("Registre o peso de cinco pessoas:")
    for i in range(1, 6):
        nome = input(Fore.CYAN + f"Digite o nome da pessoa {i}: " + Style.RESET_ALL)
        peso = ler_peso()
        pessoas.append((nome, peso))
        
        if peso > maior_peso:
            maior_peso = peso
        
        if peso < menor_peso:
            menor_peso = peso

    print(Fore.MAGENTA + "\nResumo dos pesos:")
    for nome, peso in pessoas:
        print(f"{nome}: {peso} kg")
        
    print(Fore.GREEN + f"\nO maior peso lido foi {maior_peso} kg, pertencente a:")
    for nome, peso in pessoas:
        if peso == maior_peso:
            print(nome)

    print(Fore.RED + f"\nO menor peso lido foi {menor_peso} kg, pertencente a:")
    for nome, peso in pessoas:
        if peso == menor_peso:
            print(nome)
            
    print('')

if __name__ == "__main__":
    main()