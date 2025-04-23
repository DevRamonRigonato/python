'''cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
#print('A soma vale {}'.format(s))
print(f'A soma vale {s} e foram digitados {c} vezes.')


# f - strings
'''nome = 'Rebeca'
idade = 25
salario = 10.000
print(f'O {nome:-^30} tem {idade} anos e ganha R${salario:.3f}')'''
