# Exercício Python #068 - Jogo do Par ou Ímpar
import random
from colorama import init, Fore, Style

init(autoreset=True) 

vitorias_consecutivas = 0

def imprimir_resultado(jogador_numero, computador_numero, resultado):
    print(f"Você escolheu {jogador_numero} e o computador escolheu {computador_numero}.")
    print(f"Total: {jogador_numero + computador_numero}")

    if resultado == "P":
        print(Fore.GREEN + "Você ganhou!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Você perdeu!" + Style.RESET_ALL)

while True:
    jogador = input("Escolha Par (P) ou Ímpar (I): ").strip().upper()
    if jogador not in ["P", "I"]:
        print(Fore.YELLOW + "Escolha inválida. Por favor, escolha P para Par ou I para Ímpar." + Style.RESET_ALL)
        continue

    jogador_numero = int(input("Digite um número de 1 a 10: "))
    if jogador_numero < 1 or jogador_numero > 10:
        print(Fore.YELLOW + "Número fora do intervalo permitido (1-10). Tente novamente." + Style.RESET_ALL)
        continue

    computador_numero = random.randint(1, 10)
    resultado = "P" if (jogador_numero + computador_numero) % 2 == 0 else "I"

    imprimir_resultado(jogador_numero, computador_numero, resultado)

    if jogador == resultado:
        vitorias_consecutivas += 1
    else:
        print(Fore.RED + f"Você perdeu! Vitórias consecutivas: {vitorias_consecutivas}" + Style.RESET_ALL)
        break

print(Fore.CYAN + f"Você conquistou {vitorias_consecutivas} vitória(s) consecutiva(s)." + Style.RESET_ALL)