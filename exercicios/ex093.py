matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3): # FOR de alimentação onde os valores serão colocados dentro da MATRIZ.
    for c in range(0, 3): # FOR de alimentação onde os valores serão colocados dentro da MATRIZ.
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3): # São estruturas de repetição para mostrar a estrutura da matriz na tela.
    for c in range(0, 3): # São estruturas de repetição para mostrar a estrutura da matriz na tela.
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print() # Tpda vez que terminar as colunas ele quebra pra poder fazer uma linha.
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
