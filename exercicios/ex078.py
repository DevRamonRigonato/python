núm = (int(input('Digite um número: ')), 
     int(input('Digite um número: ')), 
     int(input('Digite um número: ')), 
     int(input('Digite um número: ')), )

print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na posição {núm.index(3) + 1}ª')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
