from random import randint
from time import sleep
lista = [] # vai guardar os números sorteados, sem repetir.
jogos = [] # vai guardar TODOS os jogos sorteados
print('-' * 30)
print('      JOGA NA MEGA SENA   ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0 # é um contador para saber quantos números já foram adicionados à lista.
    while True:
        num = randint(1, 60)
        if num not in lista: # Isso evita números repetidos.
            lista.append(num) # Adiciona o número na lista.
            cont += 1 # Soma 1 ao contador, porque mais um número válido foi sorteado.
        if cont >= 6: # Quando o contador chegar a 6 ou mais, o break interrompe o laço while True.
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)