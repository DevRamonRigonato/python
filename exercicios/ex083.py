listanum = []

while True:
    num = int(input('Digite um valor: '))
    if num in listanum: # Pode colocar not in tbm, porém precisa reorganizar as mensagens e o que é feito em cada bloco.
        print('Valor duplicado! Não vou adicionar...')
    else:
        listanum.append(num)
        print('Valor adicionado com sucesso...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
listanum.sort()
print(f'Você digitou os valores {listanum}')
