'''nome_inteiro1 = str(input('Digite seu nome completo: '))
nome_maiúsculo = nome_inteiro1.upper()
nome_minúsculo = nome_inteiro1.lower()
quantia_letras = len(nome_inteiro1)
quantia_letras1nome = len(nome_inteiro1[:5])

print(nome_maiúsculo)
print(nome_minúsculo)
print(quantia_letras)
print(quantia_letras1nome)'''

nome = str(input('Digite o seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome maiúsculo é {}'.format(nome.upper()))
print('Seu nome inteiro minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format((nome.find(' '))))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))











