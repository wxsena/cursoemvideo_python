# Exercício Python #057 - Validação de Dados
from colorama import init, Fore

init(autoreset=True)

while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    
    if sexo == 'M' or sexo == 'F':
        print(Fore.GREEN + "Sexo válido: " + sexo)
        break
    else:
        print(Fore.RED + "Sexo inválido. Digite 'M' para masculino ou 'F' para feminino. Tente novamente.")