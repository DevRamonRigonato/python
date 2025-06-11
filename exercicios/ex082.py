'''valores = []
posicoes_maior = []
posicoes_menores = []
maior = menor  = 0
for i in range(0, 5):
    valor = int(input(f'Digite um valor para a Posição {i}: '))
    valores.append(valor)
    if  i == 0:
          maior = menor = valor
    else:
        if valor > maior:
                maior = valor
        if valor < menor:
              menor = valor
print(f'Você digitou os valores {valores}')
for pos, num in enumerate(valores):
      if num == maior:
            posicoes_maior.append(pos)
      else:
            if num == menor:
                  posicoes_menores.append(pos)
    
print(f'O maior valor digitado foi {maior} nas posições {posicoes_maior}')
print(f'O menor valor digitado foi {menor} nas posições {posicoes_menores}')'''

'''frutas = ['maça', 'banana', 'uva', 'laranja']
for i, fruta in enumerate(frutas):
    print(f'{i}: {fruta}')'''

'''numlista = []

for c in range(0, 5):
    numlista.append(str(input(f'Posiçao {c}: ')))
print(numlista)
for i, valor in enumerate(numlista):
   print(f'Posição {i}: {valor}')'''

'''listanum = []
for c in range(0, 5):
    listanum.append(str(input(f'Digite a palavra {c}: ')))

print('\nPalavras que começam com A:')

for i, valor in enumerate(listanum):
    if valor[0].lower() == 'a':
        print(f'Posição {i}: {valor}')'''


'''listnum = []
for c in range(0, 5):
    listnum.append(str(input(f'Digite a palavra {c}: ')))
print('\nVogais encontrada em cada palavra:')
for i, palavra in enumerate(listnum):
    print(f'Na palavra {palavra} na posição {i} temos:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()'''


'''listnum = []

for c in range(0, 5):
    listnum.append(str(input('Digite um nome de uam fruta: ')))
for i, frutas in enumerate(listnum):
    print(f'A sua posição é {i}: {frutas}')'''
    


listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]  
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c] 
print('-=' * 25)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end=' ')
print()


  