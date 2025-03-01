produto = float(input('Digite o produto '))
liquidacao = produto * 0.05 
desconto_final = produto - liquidacao

print('desconto de: {}'.format(liquidacao))
print('Preço final com desconto: R${}'.format(desconto_final))
