print('===== Prato Principal =====')
print('[1] Strogonoff')
print('[2] Carne de Panela')
print('[3] Udon')
prato = int(input('Escolha um número: '))

print('===== Bebida =====')
print('[1] Coca-Cola')
print('[2] Suco')
print('[3] Milk-Shake')
bebida = int(input('Escolha um número: '))

print('===== Sobremesa =====')
print('[1] Açai')
print('[2] Pavê')
print('[3] Bolo de Chocolate')
sobremesa = int(input('Escolha um número: '))

print('===== SEU PEDIDO FOI =====')

match prato:
    case 1:
        print('Prato principal: Strogonoff')
    case 2:
        print('Prato principal: Carne de Panela')
    case 3:
        print('Prato principal: Udon')    
    case _ :
        print('Prato principal: Opção inválida')

match bebida:
    case 1:
        print('Bebida: Coca-Cola')
    case 2:
        print('Bebida: Suco')
    case 3:
        print('Bebida: Milk-Shake')
    case _:
        print('Bebida: Opção inválida')

match sobremesa:
    case 1:
        print('Sobremesa: Açai')
    case 2:
        print('Sobremesa: Pavê')
    case 3:
        print('Sobremesa: Bolo de Chocolate')
    case _:
        print('Sobremesa: Opção inválida')

 

