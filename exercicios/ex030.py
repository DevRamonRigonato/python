print('===== \033[0;37;42mPrato Principal\033[0m =====')
print('[1] \033[0;31mStrogonoff\033[0m')
print('[2] \033[0;31mCarne de Panela\033[0m')
print('[3] \033[0;31mUdon\033[0m')
prato = int(input('\033[0;33mEscolha um número: \033[0m'))

print('===== \033[0;37;42mBebida\033[0m =====')
print('[1] \033[0;31mCoca-Cola\033[0m')
print('[2] \033[0;31mSuco\033[0m')
print('[3] \033[0;31mMilk-Shake\033[0m')
bebida = int(input('\033[0;33mEscolha um número: \033[0m'))

print('===== \033[0;37;42mSobremesa\033[0m =====')
print('[1] \033[0;31mAçai\033[0m')
print('[2] \033[0;31mPavê\033[0m')
print('[3] \033[0;31mBolo de Chocolate\033[0m')
sobremesa = int(input('\033[0;33mEscolha um número: \033[0m'))

print('===== \033[0;45mSEU PEDIDO FOI\033[0m =====')

match prato:
    case 1:
        print('Prato principal: \033[0;36mStrogonoff\033[0m')
    case 2:
        print('Prato principal: \033[0;36mCarne de Panela\033[0m')
    case 3:
        print('Prato principal: \033[0;36mUdon\033[0m')    
    case _ :
        print('Prato principal: \033[0;37;47mOpção inválida\033[0m')

match bebida:
    case 1:
        print('Bebida: \033[0;36mCoca-Cola\033[0m')
    case 2:
        print('Bebida: \033[0;36mSuco\033[0m')
    case 3:
        print('Bebida: \033[0;36mMilk-Shake\033[0m')
    case _:
        print('Bebida: \033[0;37;47mOpção inválida\033[0m')

match sobremesa:
    case 1:
        print('Sobremesa: \033[0;36mAçai\033[0m')
    case 2:
        print('Sobremesa: \033[0;36mPavê\033[0m')
    case 3:
        print('Sobremesa: \033[0;36mBolo de Chocolate\033[0m')
    case _:
        print('Sobremesa: \033[0;37;47mOpção inválida\033[0m')

 

