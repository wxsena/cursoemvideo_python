# Exercício Python #008 - Conversor de Medidas
medida = float(input("Uma distância em metros: "))
cm = round(medida * 100)
mm = round(medida * 1000)
print("A medida de {}m corresponde a {}cm e {}mm".format(medida, cm, mm))