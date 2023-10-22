# Exercício Python #052 - Números primos
numero = int(input("Digite um número inteiro: "))

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Números até {numero}:")

for i in range(1, numero + 1):
    if eh_primo(i):
        print("\033[92m", end="")
    else:
        print("\033[91m", end="")
    print(i, end=" \033[0m")