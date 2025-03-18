altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura**2)

if 18.5 <= imc < 25:
    print('Entre 18.5 e 25: Peso ideal')
elif imc < 18.5:
    print('Abaixo de 18.5: Abaixo do peso')
elif 25 <= imc < 30:
    print('25 até 30: Sobrepeso')
elif 30 <= imc < 35:
    print('30 até 35: Obesidade Grau 1')
elif 35 <= imc < 40:
    print('35 até 40: Obesidade Grau 2')
else:
    print('Acima de 40: Obesidade Grau 3')

print('Seu IMC é {:.2f}'.format(imc))
    