# Exercício Python #062 - Super Progressão Aritmética v3.0
def calcular_pa(a1, r, n):
    termos = []
    for i in range(n):
        termo = int(a1 + i * r)
        termos.append(termo)
    return termos

a1 = float(input("\033[1;36mInforme o primeiro termo da PA: \033[0m"))
r = float(input("\033[1;36mInforme a razão da PA: \033[0m"))
n = int(input("\033[1;36mQuantos termos você deseja mostrar inicialmente: \033[0m"))

termos = calcular_pa(a1, r, n)

while True:
    print("\033[1;32mTermos da PA: \033[0m", termos)

    n_adicionais = int(input("\033[1;36mQuantos termos adicionais você deseja mostrar? (0 para sair): \033[0m"))

    if n_adicionais == 0:
        break

    termos += calcular_pa(termos[-1] + r, r, n_adicionais)