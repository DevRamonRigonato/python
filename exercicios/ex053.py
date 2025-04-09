maiorpeso = 0
menorpeso = 0

for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1: 
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi de {:.2f} kg'.format(maiorpeso))
print('O menor peso lido foi de {:.2f} kg'.format(menorpeso))