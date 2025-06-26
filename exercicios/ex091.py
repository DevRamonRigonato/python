temp = []
princ = []
maiorpeso = menorpeso = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
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
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Ao todo voçê cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {maiorpeso}')
for p in princ:
    if p[1] == maiorpeso:
        print(f'peso de [{princ[0]}]')
print(f'O menor peso foi {menorpeso}')

