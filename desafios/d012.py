#produto = float(input('Digite o produto '))
#liquidacao = produto * 0.05 
#desconto_final = produto - liquidacao

#print('desconto de: {:.2f}'.format(liquidacao))
#print('Preço final com desconto: R${:.2f}'.format(desconto_final))

preço = float(input('Qual é o preço do produto? '))
novo = preço - (preço * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço,novo))
