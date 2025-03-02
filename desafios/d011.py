#altura = float(input('Digite a altura: '))
#largura = float(input('Digite a largura: '))

#area_da_parede = (altura * largura) / 2

#print('A quantidade será de: {} litros de tinta'.format(area_da_parede))

largura = float(input('Largua da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura

print('Sua parede tem a dimensão de {}x{}e sua área é de {}mm².'.format(largura, altura, área))

tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))