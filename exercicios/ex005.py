#5+3*2
#11
#5**2
#25
#5**3
#125
#19//2
#9
#19/2
#9.5
#365**522
#18%2
#0
#122%3
#2
#4**3
#64
#pow(4,3) Função interna, porém perde a ordem da procedência.
#64
#81**(1/2)
#9.0
#25**(1/2)
#5.0
#127**(1/3)
#5.026525695313479

#nome = input('Qual seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))