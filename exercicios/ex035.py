'''a = float(input('Valor casa: R$ '))
b = int(input('Quantos anos quer pagar? '))
c = float(input('Salário: R$'))
d = (a / b) / 12 # Calcula a parcela mensal

e = c * 0.3 # 30% do salário

if e >= d:
    print('Seu emprestimo foi aprovado, suas parcelas serão {:.2f}'.format(d))
else:
    print('Seu emprestimo foi recusado o valor da parcela mensal é de R${:.2f} ultrapassa 30% de sua renda mensal R${:.2f}'.format(d, e))'''

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$' ))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12) # Calcula a parcela mensal

minimo = salario * 30 / 100 # 30% do salário

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end= '')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('EMPRÉSTIMO NEGADO!')




