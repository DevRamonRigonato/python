n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('\033[0;32mO primeiro valor é maior\033[m')
elif n2 > n1:
    print('\033[0;32mO segundo valor é maior\033[m')
else:
    print('\033[0;31mNão existe valor maior, os dois são iguais\033[m')

