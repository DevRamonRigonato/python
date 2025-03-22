r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1: Forma mais intuitiva de entender!
    if r1 == r2 == r3:
        print('Os seguimentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os seguimentos acima PODEM FORMAR um triângulo ISÓSCELES!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('\033[0;31mNão PODEM FORMAR triãngulo\033[m')
