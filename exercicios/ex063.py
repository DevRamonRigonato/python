primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro # mostra o termo
cont = 1 # conta quantos termos foram
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total: 
        print('{} >'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))