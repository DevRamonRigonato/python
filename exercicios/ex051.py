frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1] #Macetizinho sem usar o for
#for letra in range(len(junto) -1, -1, -1):              #INVERSO
#    inverso += junto[letra]                             #INVERSO
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')







