#funcionario = float(input('Digite o salário atual '))
#salario_atual = funcionario * 0.15
#novo_salario = funcionario + salario_atual

#print('Salário atual: {}'.format(funcionario))
#print('Aumento de 15%: {}'.format(salario_atual))
#print('Novo salário é: R$ {}'.format(novo_salario))

salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
