a = float(input('Valor casa: '))
b = float(input('Quantos anos quer pagar: '))
c = float(input('Salário: '))
d = (a / b) / 12 # Calcula a parcela mensal

e = c * 0.3 # 30% do salário

if e >= d:
    print('Seu emprestimo foi aprovado, suas parcelas serão {:.2f}'.format(d))
else:
    print('Seu emprestimo foi recusado o valor da parcela mensal é de R${:.2f} ultrapassa 30% de sua renda mensal R${:.2f}'.format(d, e))



