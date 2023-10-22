# Exercício Python #045 - GAME: Pedra Papel e Tesoura
import random
import time
design = '=' * 30

def verificar_vencedor(escolha_usuario, escolha_computador):
    resultado = ''

    if escolha_usuario == escolha_computador:
        resultado = '\033[93mEmpate!\033[0m'
    elif (
        (escolha_usuario == 'Pedra' and escolha_computador == 'Tesoura')
        or (escolha_usuario == 'Papel' and escolha_computador == 'Pedra')
        or (escolha_usuario == 'Tesoura' and escolha_computador == 'Papel')
    ):
        resultado = '\033[92mVocê venceu!\033[0m'
    else:
        resultado = '\033[91mO computador venceu!\033[0m'

    return resultado

def exibir_jokenpo():
    print("Jokenpô - Escolha sua jogada:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

vitorias_usuario = 0
vitorias_computador = 0

for rodada in range(1, 4):
    print(f"Rodada {rodada}")

    exibir_jokenpo()
    escolha_usuario = input("Digite o número da sua escolha: ")

    if escolha_usuario not in ('1', '2', '3'):
        print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
        continue

    escolha_usuario = 'Pedra' if escolha_usuario == '1' else 'Papel' if escolha_usuario == '2' else 'Tesoura'
    print(f"Você escolheu: {escolha_usuario}")

    print("O computador está escolhendo...")
    time.sleep(2)

    escolha_computador = random.choice(['Pedra', 'Papel', 'Tesoura'])
    print(f"O computador escolheu: {escolha_computador}")

    resultado = verificar_vencedor(escolha_usuario, escolha_computador)
    print(resultado)
    print(design)

    if "Você" in resultado:
        vitorias_usuario += 1
    elif "O computador" in resultado:
        vitorias_computador += 1

if vitorias_usuario > vitorias_computador:
    print("\033[92mVocê venceu o jogo!\033[0m")
elif vitorias_usuario < vitorias_computador:
    print("\033[91mO computador venceu o jogo!\033[0m")
else:
    print("\033[93mO jogo terminou em empate!\033[0m")