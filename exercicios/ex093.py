'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma =  soma3c =  maiorvalor = 0
for l in range(0, 3):# lendo a matriz os valores, essas 3 linhas vão preencher minha matriz
    for c in range(0, 3):# lendo a matriz os valores, essas 3 linhas vão preencher minha matriz
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # lendo a matriz os valores, essas 3 linhas vão preencher minha matriz
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]                           # mostra a matriz na TELA!
        if l == 1:
            matriz[l][c] > maiorvalor
            maiorvalor = matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O mair valor da segunda linha é {maiorvalor}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]    
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0: 
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior velor da segunda linha é {maior}')





























