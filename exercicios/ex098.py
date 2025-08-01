'''ficha = {}
situacao = {}
for c in range(1):
    aluno = str(input('Nome: '))
    media = float(input(f'Média de {aluno}: '))
    ficha['nome'] = aluno
    ficha['media'] = media
    
    if ficha['media'] >= 6:
        situacao = 'Aprovado'
    elif ficha['media'] >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'
    ficha['situacao'] = situacao
print('-=' * 30)
for k, v in ficha.items():
    print(f'{k.capitalize()}:  {v}')'''

aluno = {}

aluno ['nome'] = str(input('Nome: '))
aluno ['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno ['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print(aluno)