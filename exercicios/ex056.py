media_idade = 0
soma_idade = 0
homemidade_velho = 0
velhohomem = ''
tot_mulher = 0
for p in range(1, 5):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    media_idade += idade
    if p == 1 and sexo in 'Mm':
        homemidade_velho = idade
        velhohomem = nome
    if sexo in 'Mm' and idade > homemidade_velho:
        homemidade_velho = idade
        velhohomem = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher += 1 #tot_mulher = tot_mulher + 1

soma_idade = media_idade / 4
print('\033[0;32mA média idade do grupo é {} anos\033[m'.format(soma_idade))
print('\033[0;32mO homem mais velho chama {} e tem {} anos de idade.\033[m'.format(velhohomem, homemidade_velho))
print('\033[0;32mTem no total {} mulheres menores de idade.\033[m'.format(tot_mulher))



