soma = totproduto = menor = cont = 0
barato = ''

print('-' * 20)
print('SUPER BARATAÃO')
print('-' * 20)
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preço = float (input('Preço: R$'))
    cont += 1
    soma += preço
    barato = ''
    if preço > 1000:
        totproduto += 1
    if cont == 1: #or preço < menor: revisar!!!
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compra foi R${soma:.2f}')
print(f'Temos {totproduto} custando mais de R$1000.00 reais')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')