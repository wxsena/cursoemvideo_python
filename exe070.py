# Exercício Python #070 - Estatísticas em produtos
from termcolor import colored

produtos = []
total_gasto = 0

def mostrar_resumo():
    print(colored("\nResumo da compra:", "cyan"))
    for produto, preco in produtos:
        print(colored(f"{produto}: R$ {preco:.2f}", "green"))
    print(colored(f"Total gasto: R$ {total_gasto:.2f}", "green"))

def encontrar_produto_mais_caro():
    if not produtos:
        print(colored("A lista de produtos está vazia.", "red"))
        return
    produto_mais_caro = max(produtos, key=lambda x: x[1])
    print(colored(f"Produto mais caro: {produto_mais_caro[0]} (R$ {produto_mais_caro[1]:.2f})", "green"))

while True:
    print(colored("\nOpções:", "cyan"))
    print(colored("1. Adicionar produto", "cyan"))
    print(colored("2. Visualizar resumo da compra", "cyan"))
    print(colored("3. Encontrar produto mais caro", "cyan"))
    print(colored("4. Sair", "cyan"))

    escolha = input(colored("Escolha uma opção: ", "yellow"))

    if escolha == "1":
        nome_produto = input(colored("Digite o nome do produto: ", "cyan"))
        try:
            preco_produto = float(input(colored("Digite o preço do produto: R$ ", "cyan")))
        except ValueError:
            print(colored("Preço inválido. Insira um valor numérico.", "red"))
            continue
        produtos.append((nome_produto, preco_produto))
        total_gasto += preco_produto
        print(colored(f"{nome_produto} adicionado à lista.", "green"))

    elif escolha == "2":
        mostrar_resumo()

    elif escolha == "3":
        encontrar_produto_mais_caro()

    elif escolha == "4":
        print(colored("Saindo do programa. Obrigado!", "magenta"))
        break

    else:
        print(colored("Escolha inválida. Por favor, escolha uma opção válida.", "red"))