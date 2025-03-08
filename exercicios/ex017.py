num = int(input('Informe um número: '))
print('Analisando o número {:.0f}'.format(num))
unidade = num % 10
print('Unidade: {:.0f}'.format(unidade))
dezena = (num // 10) % 10
print('Dezena: {:.0f}'.format(dezena))
centena = (num // 100) % 10
print('Centena: {:.0f}'.format(centena))
milhar = (num // 1000) % 10
print('Milhar: {:.0f}'.format(milhar))