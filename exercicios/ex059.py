from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entra 0 e 10.
Será que você consegue advinhar qual foi ?''')
acertou = False # Ainda não acertou
palpites = 0
while not acertou: # Enquanto acertou for FALSO, o laço continua rodando.
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True # Agora acertou, então o while vai parar na próxima rodada
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
            if jogador > computador:
                print('Menos... Tente mais uma vez.')
print('Parabéns acerto com {} tentativas. Parabéns!'.format(palpites))

