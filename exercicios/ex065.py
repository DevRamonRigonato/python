n = 0
soma = 0
numeros_digitados = 0
while n != 999: 
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        numeros_digitados += 1
print('Voçê digitou {} números e a soma entre eles foi {}'.format(numeros_digitados, soma))