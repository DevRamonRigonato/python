'''largura = 25
print('=' * 25)
print('10 TERMOS DE UMA PA'.center(largura))
print('=' * 25  )

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for i in range(0, 10):
  termo = p1 + i * r
  print('{}'.format(termo), end=' → ')
print('ACABOU')'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
  print('{}'.format(c), end=' → ')
print('ACABOU')    