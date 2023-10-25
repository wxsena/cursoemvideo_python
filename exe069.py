# Exercício Python #069 - Análise de dados do grupo
from colorama import init, Fore, Style

init(autoreset=True)

pessoas_mais_dezoito = 0
homens_cadastrados = 0
mulheres_menos_vinte = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M para masculino e F para feminino): ").strip().upper()

    if idade > 18:
        pessoas_mais_dezoito += 1

    if sexo == 'M':
        homens_cadastrados += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1

    continuar = input(Fore.BLUE + "Deseja continuar cadastrando? (S para Sim, qualquer outra tecla para encerrar): " + Style.RESET_ALL).strip().upper()
    if continuar != 'S':
        break

print(Fore.GREEN + f"A) {pessoas_mais_dezoito} pessoa(s) tem mais de 18 anos." + Style.RESET_ALL)
print(Fore.CYAN + f"B) {homens_cadastrados} homem(s) foram cadastrados." + Style.RESET_ALL)
print(Fore.MAGENTA + f"C) {mulheres_menos_vinte} mulher(es) tem menos de 20 anos." + Style.RESET_ALL)