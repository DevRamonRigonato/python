'''oposto1 = float(input('Comprimento do cateto oposto: '))
adjacente2 = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (oposto1 ** 2 + adjacente2 **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))

