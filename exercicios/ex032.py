nome = str(input('Qual é seu nome? '))

if nome == 'Ramon':
    print('Que nome bonito')
elif nome == 'Danielle' or nome == 'Milena' or nome == 'Rebeca':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Jesus Deus Neriah':
    print('É o nome mais lindo que já existiu.')
else:
    print('Seu nome é normal.')
