listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 40)
for pos in range(0, len(listagem)): # cria uma sequência de números de 0 até o tamanho da tupla.
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') # serve para mostrar apenas os nomes dos produtos.
    else:
        print(f'R${listagem[pos]:>7.2f}') # serve para mostrar apenas os preços dos produtos.
print('-' * 40)
    