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

nomes = []
idades = []

for i in range(4):
    nome = str(input('Digite o nome: ')).strip().upper()
    idade = int(input('Digite a idade: '))
    nomes.append(nome)
    idades.append(idade)
for i in range(len(nomes)):
    print(f'{nomes[i]} tem {idades[i]} anos.')


    
