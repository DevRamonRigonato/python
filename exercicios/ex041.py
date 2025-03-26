print ('{:=^40}'.format (' LOJAS MONCARA '))
compras = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Escolha a opção de pagamento: '))

if opcao == 1:
    total = compras - (compras * 10 / 100) # 10% de desconto
elif opcao == 2:
    total = compras - (compras * 5 / 100) # 5% de desconto
elif opcao == 3:
    total = compras
    print('Sua compra parcelada em 2x de R${:.2f} SEM JUROS.'.format(total / 2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = compras + (compras * 20 / 100) # 20% de juros
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, total / parcelas))
else:
    total = compras
    print('\033[0;31mOpção inválida!\033[m')

print(f'Sua compra de R${compras:.2f} vai custar R${total:.2f} no final.')




