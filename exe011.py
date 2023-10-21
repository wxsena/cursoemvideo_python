# Exercício Python #011 - Pintando Parede
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

print(f"Sua parede possui a dimensão {largura} x {altura} e sua área é de: {altura * largura}m²")

tinta = (altura * largura) / 2
print(f"Para pintar essa parede você vai precisar de {tinta}l de tinta")