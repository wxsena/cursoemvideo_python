# Exercício Python #043 - Índice de Massa Corporal
peso = float(input('Por favor, insira seu peso (em Kg): '))
altura = float(input('Por favor, insira sua altura (em metros): '))

imc = peso / (altura ** 2)

print('Seu IMC é: {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 24.9:
    print('Parabéns, você está na faixa de peso normal.')
elif 25 <= imc < 29.9:
    print('Você está em sobrepeso.')
else:
    print('Você está em obesidade. Recomendamos que consulte um médico.')
