# Exercício Python #053 - Detector de Palíndromo
import re

def remover_caracteres_especiais(frase):
    return re.sub(r'[^a-zA-Z0-9]', '', frase)

def eh_palindromo(frase):
    frase = remover_caracteres_especiais(frase).lower()
    return frase == frase[::-1]

def imprimir_mensagem_palindromo(palindromo):
    if palindromo:
        print("\033[92mA frase é um palíndromo.\033[0m")  # Verde
    else:
        print("\033[91mA frase não é um palíndromo.\033[0m")  # Vermelho

frase = input("Digite uma frase: ")

resultado = eh_palindromo(frase)
imprimir_mensagem_palindromo(resultado)

frase_sem_espacos = remover_caracteres_especiais(frase)
frase_invertida = frase_sem_espacos[::-1]

print(f"Frase sem espaços e caracteres especiais: {frase_sem_espacos}")
print(f"Frase invertida: {frase_invertida}")