# Exercício Python #067 - Tabuada v3.0
from colorama import init, Fore, Style

init(autoreset=True)

while True:
    numero = int(input("Digite um número para ver a tabuada (digite um número negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado. Obrigado!")
        break
    
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero:02} x {i:02} = {Fore.GREEN}{resultado:2}{Style.RESET_ALL}")