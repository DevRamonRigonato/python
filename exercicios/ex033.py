'''nome = str(input('Digite o nome do aluno: '))
p1 = float(input('Digite a nota da P1: '))
p2 = float(input('Digite a nota da P2: '))
media = (p1 + p2) / 2
    
if media >= 7.0:
    print('Média 7.0 ou superior:'
    ' APROVADO')
elif media > 5.0 and 6.9:
    print('Média entre 5.0 e 6.9: '
    'você está de RECUPERAÇÃO')
else:
    print('Média de 5.0: '
    'REPROVADO!')
print(media)'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segudna nota: '))
media = (n1 + n2) / 2

if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')









