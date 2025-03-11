distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
    
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))

#preço = distância * 0.50 if distância <= 200 else distância * 0.45



