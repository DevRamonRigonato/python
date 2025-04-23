num = soma = cont = 0
while num != 999:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1 
print(f'A soma dos {cont} foi {soma}')

