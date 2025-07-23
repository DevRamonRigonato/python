'''nomes = ['Ramon', 'Rebeca', 'Danielle', 'Milena','Aryelle']
print(len(nomes))
print(nomes[0])
print(nomes[4])
print(nomes[len(nomes) - 1])'''

'''nomes = ['Ramon', 'Rebeca', 'Milena', 'aiaiaiia']

indice = int(input('Digite um número (índice): '))
if indice < len(nomes):
    print(f'O nome é {nomes[indice]}')
else:
    print('Índice inválido!')'''

'''nomes = ['Saori', 'Sayuri', 'Hinata', 'Yui']
for i in range(len(nomes)):
    print(f'{i} - {nomes[i]}')'''

'''nomes = ['Saori', 'Sayuri', 'Hinata', 'Yui']

for i, nome in enumerate(nomes):
    print(f'{i} - {nome}')'''

'''pessoas = ['Lara', 'João', 'Carlos', 'Amanda', 'Renata']

for i, nome in enumerate(pessoas):
    if i % 2 == 0:
        print(f'{i} - {nome} (índice par)')
    else:
        print(f'{i} - {nome} (índice impar)')'''

'''nomes = []
idades = []
maivelho = mainovo = 0
for i in range(3):
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite a idade: '))
    nomes.append(nome)
    idades.append(idade)
    if i == 0:
        maivelho = mainovo = idade
    else:
        if idade > maivelho:
            maivelho = idade
        if idade < mainovo:
            mainovo = idade

print('\n- - - Lista de pessoas - - -')
for i in range(len(nomes)):
    print(f'{nomes[i]} tem {idades[i]} anos')

for nome in nomes:
    if nome[0].upper() == 'A':
        print(f'{nome} começa com A')

print(f'\nPessoa mais velha tem {maivelho} anos')
print(f'Pessoa mais nova tem {mainovo} anos')'''

'''nomes = []
idades = []

for i in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    nomes.append(nome)
    idades.append(idade)

print('\n--- Lista de pessoas ---')
for i in range(len(nomes)):
    print(f'{nomes[i]} - {idades[i]} anos')

# calcula e mostra média de idades
media = sum(idades) / len(idades)
print(f'\nMédia de idade: {media:.1f} anos')

# mostra quem tem 18 anos ou mais
print('\nPessoas com 18 anos ou mais:')
for i in range(len(idades)):
    if idades[i] >= 18:
        print(f'{nomes[i]} - {idades[i]} anos')

for nome in nomes:
    if len(nomes) <= 5:
        print(nome)'''


'''listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-=' * 30)
print(f'Os valores digitados foram: {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()'''

'''pares = []
impares = []
for c in range(7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')'''

'''numlista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in numlista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numlista.append(valor)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
numlista.sort()
print(numlista)'''

'''numeros = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(numeros)'''

'''lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')'''

'''lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {(lista)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')'''

'''lista = []
pares = []
impares = []
while True:
    valor = int(input('Digite um número: '))
    
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    lista.append(valor)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break   
lista.sort(reverse=True)
pares.sort()
impares.sort()
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')'''

'''expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')'''

'''teste = list()
teste.append('Ramon')
teste.append(26)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in (galera):
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

'''galera = []
dados = []
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Ao todo temos {totmai} maior de idade e {totmen} menor de idade.')'''

'''galera = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':    
        break

print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {mai}.Kg ',end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {men}.Kg ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()'''

num = [[], []]

for c in range(0, 7):
    valor  = int(input(f'Digite o {c+1}°. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
print(f'Os valores pares digitados foram {num[0]}')
num[1].sort()
print(f'Os valores impares digitados foram {num[1]}')
