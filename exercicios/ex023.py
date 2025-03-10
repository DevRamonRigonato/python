'''velocidade = float(input('Qual a valocidade atual do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h. \nVocê deve pagar uma multa de R$ {:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')''' 
#EXERCÍCIO MAU RESOLVIDO!!!!!!!

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de $${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

