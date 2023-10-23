# Exercício Python #058 - Jogo da Adivinhação v2.0
import random
from colorama import init, Fore

init(autoreset=True)

vitorias = 0
derrotas = 0

def jogar_jogo():
    global vitorias, derrotas

    numero_aleatorio = random.randint(0, 10)
    max_tentativas = 3

    print(Fore.MAGENTA + '=' * 33)
    print(Fore.MAGENTA + "Bem-vindo ao Jogo de Adivinhação!")
    print("O computador pensou em um número entre 0 e 10. Tente adivinhar.")

    tentativas = 0
    acertou = False

    while tentativas < max_tentativas and not acertou:
        try:
            palpite = int(input("Digite um número: "))
            tentativas += 1

            if palpite == numero_aleatorio:
                print(Fore.GREEN + f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativa(s).")
                vitorias += 1
                acertou = True
            elif palpite < numero_aleatorio:
                print(Fore.RED + "Tente um número maior.")
            else:
                print(Fore.RED + "Tente um número menor.")

        except ValueError:
            print(Fore.RED + "Por favor, insira um número válido.")

    if not acertou:
        print(Fore.RED + f"Você atingiu o limite de {max_tentativas} tentativas. O número era {numero_aleatorio}.")
        derrotas += 1

    print(Fore.CYAN + f"Vitórias: {vitorias}, Derrotas: {derrotas}")

    return jogar_novamente()

def jogar_novamente():
    while True:
        escolha = input(Fore.BLUE + "Deseja jogar novamente? (S/N): ").upper()
        if escolha == 'S':
            return True
        elif escolha == 'N':
            print(Fore.GREEN + "Obrigado por jogar. Até a próxima!")
            return False
        else:
            print(Fore.RED + "Por favor, escolha 'S' para jogar novamente ou 'N' para sair.")

if __name__ == "__main__":
    continuar = True
    while continuar:
        continuar = jogar_jogo()