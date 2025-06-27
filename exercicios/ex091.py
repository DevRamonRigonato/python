temp = [] # lista temporária que guarda o nome e peso da pessoa atual.
princ = [] # lista principal que guarda todas as pessoas cadastradas.
maiorpeso = menorpeso = 0 # vão armazenar o maior e o menor peso cadastrados.
while True:
    temp.append(str(input('Nome: '))) # Pede o nome da pessoa e coloca em temp[0].
    temp.append(float(input('Peso: '))) # Pede o peso da pessoa e coloca em temp[1].
    if len(princ) == 0:
        maiorpeso = menorpeso = temp[1]
    else:
        if temp[1] > maiorpeso:
            maiorpeso = temp[1]
        if temp[1] < menorpeso:
            menorpeso = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ',end='')
for p in princ:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
print()

'''num = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}°. valor: '))
    if num % 2 == 0:'''
