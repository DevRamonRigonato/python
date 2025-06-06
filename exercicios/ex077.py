from random import randint
números = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')

