#num = int(input('Digite um número: '))
#centimetros = num * 100
#milimetros = num * 1000

#print('O valor convertido em centímetro é: {}'.format(centimetros))
#print('O valor convertido em milímetros é: {}'.format(milimetros))

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))