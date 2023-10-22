# Exercício Python #056 - Analisador completo
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(Fore.RED + "Valor inválido. Por favor, insira um número inteiro válido." + Style.RESET_ALL)

def ler_sexo():
    while True:
        sexo = input(Fore.CYAN + "Sexo (M para masculino, F para feminino): " + Style.RESET_ALL).upper()
        if sexo in ('M', 'F'):
            return sexo
        else:
            print(Fore.RED + "Sexo inválido. Digite 'M' para masculino ou 'F' para feminino." + Style.RESET_ALL)

# Inicializa as variáveis
soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
contagem_mulheres_menos_20 = 0

# Loop para ler os dados de 4 pessoas
for i in range(1, 5):
    print(Fore.YELLOW + f"Digite os dados da pessoa {i}:" + Style.RESET_ALL)
    nome = input(Fore.CYAN + "Nome: " + Style.RESET_ALL)
    idade = ler_int(Fore.CYAN + "Idade: " + Style.RESET_ALL)
    sexo = ler_sexo()

    soma_idades += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        contagem_mulheres_menos_20 += 1

# Calcula a média de idade
media_idade = soma_idades / 4

# Mostra os resultados
print(Fore.MAGENTA + ("="*40) + Style.RESET_ALL)
print(Fore.GREEN + f"A média de idade do grupo é {media_idade:.2f} anos." + Style.RESET_ALL)
if nome_homem_mais_velho:
    print(Fore.GREEN + f"O homem mais velho se chama {nome_homem_mais_velho} e possui {idade_homem_mais_velho} anos." + Style.RESET_ALL)
else:
    print(Fore.RED + "Não foi informado nenhum homem." + Style.RESET_ALL)
if contagem_mulheres_menos_20 == 1:
    print(Fore.GREEN + "1 mulher tem menos de 20 anos." + Style.RESET_ALL)
else:
    print(Fore.GREEN + f"{contagem_mulheres_menos_20} mulheres têm menos de 20 anos." + Style.RESET_ALL)
print(Fore.MAGENTA + ("="*40) + Style.RESET_ALL)