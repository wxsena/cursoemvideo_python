# Exercício Python #018 - Seno, Cosseno e Tangente
from math import radians
from math import sin
from math import cos
from math import tan

try:
    ângulo = float(input("Digite o número: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido.")
    ângulo = 0

seno = sin(radians(ângulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(ângulo, seno))

cosseno = cos(radians(ângulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ângulo, cosseno))

tangente = tan(radians(ângulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ângulo, tangente))