# Exercício Python #063 - Sequência de Fibonacci v1.0
from colorama import Fore, Style, init
init(autoreset=True)

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

N = int(input("Digite o valor de N: "))
fibonacci_sequence = fibonacci(N)

for number in fibonacci_sequence:
    if number % 2 == 0:
        print(Fore.GREEN + str(number), end=" - ")
    else:
        print(Fore.BLUE + str(number), end=" - ")

print(Style.RESET_ALL)