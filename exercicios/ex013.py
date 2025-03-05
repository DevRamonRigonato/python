from random import choice, randint, shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segudo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
apresentação = shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))