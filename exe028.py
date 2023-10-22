# Exercício Python #028 - Jogo da Adivinhação v.1.0
import random 
from time import sleep

computador = random.randint(1, 5)
print("==="*10)
user = int(input("Em qual número estou pensando (de 0 a 5)? "))
print("Processando...")
sleep(3)

if user == computador:
    print("Parabéns! Você acertou o número!")
else:
    print("Você perdeu! O número era {}, boa sorte na próxima.".format(computador))
print("==="*10)