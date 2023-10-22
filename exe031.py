# Exercício Python #031 - Custo da Viagem
from time import sleep

# Definir constantes para as taxas de preço
TAXA_PADRAO = 0.50
TAXA_PROMOCIONAL = 0.45

# Solicitar a distância da viagem
distancia = float(input("Qual é a distância da sua viagem? "))

# Verificar se a distância é positiva
if distancia < 0:
    print("A distância não pode ser negativa. Por favor, insira um valor válido.")
else:
    sleep(3)
    print("Você está prestes a começar uma viagem de {}km!".format(distancia))
    print("Calculando a passagem...")
    sleep(5)
    
    # Calcular o preço com base na distância
    preco = distancia * TAXA_PADRAO if distancia <= 200 else distancia * TAXA_PROMOCIONAL
    
    print("E o preço da sua passagem será de R${:.2f}".format(preco))