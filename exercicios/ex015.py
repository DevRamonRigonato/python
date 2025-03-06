lista_nome = []
lista_p1 = []
lista_p2 = []
lista_media = []
lista_situacao = []

for i in range(4):
    nome = input('Digite o nome do aluno: ')
    lista_nome.append(nome)

    p1 = float(input('Digite nota da P1: '))
    lista_p1.append(p1)

    p2 = float(input('Digite a nota da P2: '))
    lista_p2.append(p2)

    media = (p1 + p2) / 2
    lista_media.append(media)

    if media >= 6.0:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    lista_situacao.append(situacao)  

    print('\Resultados:')
    for i in range(4):
        print('Aluno: {}, Média: {}, Situação: {}'.format(lista_nome, lista_media, lista_situacao))





'''for i in range(100):
    print('Essa é a {}ª vez que o loop está rodando'.format(i+1))'''

'''lista_nomes = []
lista_nomes.append('Ramon')
lista_nomes.append('Rebeca')
lista_nomes.append('Danielle')
print(lista_nomes)'''

'''nota = 5

if nota >= 6:
    print('Aprovadissssiiiiiiiiimmmmmaaaaa!!!!!')
else:
    print('I am sorry, what pity REPROVADO!!!!!')'''






