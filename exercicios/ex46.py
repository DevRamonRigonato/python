soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador += 1
        soma += i
print('\033[0;32mA soma de todos os {} valores solicitados é {}\033[m'.format(contador, soma))