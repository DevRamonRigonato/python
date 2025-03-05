'''import random
aluno1 =(input('Primeiro aluno: '))
aluno2 =(input('Segundo aluno: '))
aluno3 =(input('Terceiro aluno: '))
aluno4 =(input('Quarto aluno: '))

alunos = (aluno1, aluno2, aluno3, aluno4)
aluno_escolhido = random.randint(0, 4)

print('O aluno escolhido foi {}'.format(alunos[aluno_escolhido]))'''

from random import choice
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = n1, n2, n3, n4
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
