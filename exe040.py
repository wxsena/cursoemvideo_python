# Exercício Python #040 - Aquele clássico da Média
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media >= 7:
    print('O aluno está APROVADO.')
elif 5 <= media < 7:
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')