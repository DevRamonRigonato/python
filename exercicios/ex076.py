tabela = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Fluminense', 'Bahia', 'Mirassol', 'Atlético-MG', 'Botafogo', 'Ceará SC', 'Corinthians', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco da Gama', 'EC Vitória', 'Fortaleza', 'Santos', 'Juventude', 'Sport Recife')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 15)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 15)
print(f'O Atlético-MG está na {tabela.index("Atlético-MG") + 1}ª posição')


