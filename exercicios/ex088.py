'''dados = []
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])'''
'''teste = []
teste.append('Ramon')
teste.append(26)
galera = []
galera.append(teste[:])
teste[0] = 'Rebeca'
teste[1] = 24
galera.append(teste[:])
print(galera)'''
'''galera = [['Ramon', 26], ['Rebeca', 24], ['Danielle', 25], ['Milena', 26]]
print(galera[0][0])'''
'''galera = [['Ramon', 26], ['Rebeca', 24], ['Danielle', 25], ['Milena', 26]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''
galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ').strip().upper()))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
