# Exercício Python #014 - Conversor de Temperaturas
celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = celsius * 9/5 + 32
print("{:.2f}ºC corresponde a {:.2f}°F.".format(celsius, fahrenheit))