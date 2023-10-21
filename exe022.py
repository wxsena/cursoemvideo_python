# Exercício Python #022 - Analisador de Textos
frase = str(input("Digite um nome: "))
print("Analisando seu nome... ")
print("Seu nome em maiúsculo é {}.".format(frase.upper()))
print("Seu nome em minúsculo é {}.".format(frase.lower()))
print("Seu nome possui {} letras.".format(len(frase)))
separa = frase.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0])))