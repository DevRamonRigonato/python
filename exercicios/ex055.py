somaidade = 0 # 25 + 30 + 35 + 40  # Total = 130 - vai somar todas as idades
mediaidade = 0 # vai guardar a média final
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5): # repete 4 vezes
    print('{}° PESSOA'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    somaidade += idade # soma a idade da pessoa atual
    if p == 1 and sexo in 'Mn': # Primeira pessoa homem OBS: CÓDIGO ZUADO!!!!!!!
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem: # Verifica se a pessoa é do sexo masculino E se tem idade maior que o homem mais velho até agora
        maioridadehomem = idade # Atualiza a variável com a nova maior idade masculina encontrada
        nomevelho = nome # Salva o nome dessa pessoa como sendo o homem mais velho até agora
    if sexo in 'Ff' and idade < 20: # Se for mulher com menos de 20 anos, incrementa o contador
        totmulher20 += 1

mediaidade = somaidade / 4 # calcula a média após o loop
print('A média da idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheeres com menos de 20 anos'.format(totmulher20))