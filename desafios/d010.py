#carteira = float(input('Quantos reais você tem? '))
#dolar = carteira / 5.85

#print('Você pode comprar apenas: {:.2f} dolares'.format(dolar))

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.85

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))