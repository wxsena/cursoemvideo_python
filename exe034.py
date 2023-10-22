# Exercício Python #034 - Aumentos múltiplos
salario = float(input("Qual é o salário do funcionário? "))

aumento1 = salario * 1.10
aumento2 = salario * 1.15

if salario > 1250:
    print("O novo salário é de R$ {:.2f} com um aumento de 10%.".format(aumento1))
else:
    print("O novo salário é de R$ {:.2f} com um aumento de 15%.".format(aumento2))