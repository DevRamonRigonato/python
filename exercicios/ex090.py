num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}°. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores PARES digitados foram {num[0]}')
print(f'Os valores ÍMPARES digitados foram {num[1]}')
