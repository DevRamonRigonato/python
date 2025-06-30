'''temp = []
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
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
print()'''

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}°. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores Ímpares digitados foram: {num[1]}')
    