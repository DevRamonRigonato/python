primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro # mostra o termo
cont = 1 # conta quantos termos foram
while cont <= 10: 
    print('{} >'.format(termo), end=' ')
    termo += razao
    cont += 1

