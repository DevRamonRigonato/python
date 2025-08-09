pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa ['nome'] = str(input('Nome: '))
    while True:
        pessoa ['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if pessoa ['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa ['idade'] = int(input('Idade: '))
    soma += pessoa ['idade']
    galera.append(pessoa.copy())
    resp = ' '
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
            break
media = soma / len(galera)
print('-=' * 30)
print(f'A) Ao todo tem {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.') 
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
     if p ['sexo'] == 'F':
          print(f'{p["nome"]} ', end='')
print()
print('D) A lista de pessoas que estão acima da média: ')
for p in galera:
     if p ['idade'] >= media:
          print('    ')
          for k, v in p.items():
              print(f'{k} = {v}; ', end='')  
          print()
print('<< ENCERRADO >>')      
            