#dias_alugados = int(input('Quantos dias alugados? '))
#km = float(input('Quantos Km rodados? '))
#aluguelcarros = (dias_alugados * 60) 
#kmrodado = (km * 0.15) + aluguelcarros
#print('O total a pagar é de: R${}'.format(kmrodado))

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))

