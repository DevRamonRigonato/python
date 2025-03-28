#from random import randint
#print('''Suas opções: 
#[ 0 ] PEDRA
#[ 1 ] PAPEL
#[ 2 ] TESOURA''')
#computador = randint(0,2)
#jogador = int(input('Qual é sua jogada? '))
#print('Computador jogou: {}'.format(computador))
#if jogador == computador:
#    print('EMPATE!')
#elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
#    print('VOCÊ VENCEU!')
#else:
 #   print('VOCÊ PERDEU!')

from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:   
[ 0 ]
[ 1 ]
[ 2 ]''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: #Computador jogou PEDRA
 if jogador == 0:
  print('EMPATE') 
 elif jogador == 1:
  print('Jogador Vence')
 elif jogador == 2:
  print('Computador VENCE')
 else:
  print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador jogou PAPEL
 if jogador == 0:
  print('Computador VENCE')
 elif jogador == 1:
  print('EMPATE')
 elif jogador == 2:
    print('Jogador VENCE')
 else:
  print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador jogou TESOURA
 if jogador == 0:
  print('Jogador VENCE')
 elif jogador == 1:
  print('Computador VENCE')
 elif jogador == 2:
  print('EMPATE')
 else:
  print('JOGADA INVÁLIDA')