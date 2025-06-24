temp = []
princ = []
maiorp = menorp = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0: # A gente usa len() nesse caso para verificar se a lista está vazia.
        maiorp = menorp = temp[1]
    else:
        if temp[1] > maiorp:
            maiorp = temp[1]
        if temp[1] < menorp:
            menorp = temp[1]
    princ.append(temp[:])
    temp.clear() # limpa antes de reutilizar
  
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O mair peso foi de {maiorp}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorp}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='' )
print()
