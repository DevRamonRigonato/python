'''a = 7
b = "42"
c = False
d = 3.5
e = '7.5'

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''

'''x = '10'
y = 10
resultado = int(x) + y
print(resultado)'''

'''num = int(input('Digite um número: '))
s = num + 1
a = num - 1
print(f'Analisando o valor {num} seu antecessor é {a} e o sucessor é {s}')'''

'''num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f'O drobro de {num} é {dobro}.')
print(f'O triplo de {num} é {triplo}.')
print(f'A raiz quadrada de {num} é {raiz:.2f}.')'''

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {media}')'''

'''num = float(input('Uma distância em metros: '))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000
print(f'A medida de {num}m corresponde a {km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm')'''

'''print('=' * 20)  
print('{:^20}'.format('TABUADA'))
print('=' * 20) 

num = int(input('Digite um número: '))
print(f'{num} x 1 = {num *1}')
print(f'{num} x 2 = {num *2}')
print(f'{num} x 3 = {num *3}')
print(f'{num} x 4 = {num *4}')
print(f'{num} x 5 = {num *5}')
print(f'{num} x 6 = {num *6}')
print(f'{num} x 7 = {num *7}')
print(f'{num} x 8 = {num *8}')
print(f'{num} x 9 = {num *9}')
print(f'{num} x 10 = {num *10}')'''


'''num = float(input('Quanto dinheiro você tem na carteira? R$'))
cotacao = num / 5.68
print(f'Com R${num} você pode comprar US${cotacao}')'''

'''largura = float(input('Largura da parede: '))
altura = float(input('Altura da parece: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura} e {altura} e a sua área é de {area}m')
tinta = area / 2
print(f'Para pintar essa parede, vocè precisará de {tinta}l de tinta')'''

'''preço = float(input('Qual o preço do produto? R$'))
novo =  preço - (preço * 5 / 100)
print(f'O pruduto que custava R${preço}, na promoção com desconto de 5% vai custar R$ R${preço}')'''

'''num = float(input('Qual é o salario do funcionario? R$'))
salario =  num + (num * 15 / 100)
print(f'Um funcionario que ganhava R${num} com 15% de aumento, passa a receber R${salario}')'''

'''c = float(input('Informe a temperatura em °C: '))
f = ((9*c)/5) + 32
print(f'A temperatura de {c} corresponde a {f}')'''

'''dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15) 
print(f'O total a pagar é de R${total}')'''

'''import math #from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')'''
'''from math import trunc
n = float(input('Digite um valor: '))
valor = trunc(n)
print(f'O valor digitado foi {n} e a sua porção inteira é {valor}')'''

'''from math import hypot
opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hipo = (opo ** 2 + adj **2) ** 0.5 # hypot(co, ca)
print(f'A hipotenusa vai medir {hipo:.2f}')'''

'''import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')'''

'''from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print(f'O aluno escolhido foi {sorteio}')'''

'''from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentção será')
print(lista)'''


'''frase = 'Curso em Vídeo Python'
print(frase[9::3])'''

'''frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2] [3])'''

'''nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')'''

'''n = int(input('Informe um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezana: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')'''

'''nome = str(input('Em que cidade você nasceu? ')).strip()
cidade = nome[:5].upper() == 'SANTO'
print(cidade)'''


'''n = str(input('Qual é seu nome completo? ')).strip()
nome = 'RIGONATO' in n.upper()
print(f'Seu nome tem Rigonato? {nome}')'''

'''frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A') + 1}')
print(f'A última letra apareceu na posição {frase.rfind('A') + 1}')'''

'''n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome) - 1]}') '''


'''from random import choice
n1 = str(input('Digite o nome do Primeiro aluno: ')).strip().upper()
n2 = str(input('Digite o nome do Segundo aluno: ')).strip().upper()
n3 = str(input('Digite o nome do Terceiro aluno: ')).strip().upper()
n4 = str(input('Digite o nome do Quarto aluno nome: ')).strip().upper()
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print(f'O nome do aluno sorteado é {sorteio}')'''

'''from random import randint
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=' * 30)
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS! Você conseguiu me VENCER!')
else:
    print(f'QUE PENA! Eu pensei no número {computador} e não no {jogador}')'''

   

'''velocidade = int(input('Qual a velocidade atual do carro? '))
muta = (velocidade - 80) * 7
if velocidade > 80:
    print(f'''
'''MULTADO! Você excedeu o limite permitido que é de 80Km/h
Você deve pagar uma multa de R${muta}!
Tenha um bom dia e dirija com Segurança!'''
''')
else:
    print('Tenha um BOM DIA e dirija com segurança!!!')'''

'''n = int(input('Me diga um número qualquer: '))
if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é ímpar')'''

'''distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')'''

'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {menor} e o maior {maior}')'''

'''salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2F} passa a ganhar R${novo:.2f} agora.')'''

'''r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo! ')'''

'''nome = str(input('Digite seu nome: ')).upper()
if nome == 'RAMON':
    print('Que nome celestial! Tenha um, BOM DIA!')
elif nome in 'REBECA MILENA DANIELLE':
    print('Voce É linda, quero muito vc!')
elif nome == 'PAULO' or nome == 'DANILO' or nome == 'BOI':
    print('Não gosto de voce')

else:
    print('Tenha um, BOM DIA!')'''



'''casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
ano = int(input('Em quantos anos vai pagar? '))
prestação =  casa / (ano * 12)
minimo = salario * 30 / 100
print(f'Para pagar a casa de R${casa} em {ano} anos', end=' ')
print(f'A prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!') '''


"""num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] converter para BINÁRIO 
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido pra BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção invalida. Tente novamente.')"""

'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O primeiro valor é MAIOR')
elif n2 > n1:
    print('O segundo valor é MENOR')
elif n1 == n2:
    print('Os números são IGUAIS')'''

'''from datetime import date
sexo = str(input('H ou F: ')).upper()
if sexo in 'H':
    print('continue')
else:
    if sexo in 'F':
     print('Voce n precisa')
    exit()
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = ano_at9ual + saldo 
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado há {saldo} anos')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}')'''

'''from datetime import date
from time import sleep
sexo = str(input('Digite o seu sexo. [H/M] ')).strip().upper()
if sexo == 'H':
    print('Está preparado para SOFRER CAMPEÃO?')
elif sexo == 'M':
    print('Donzela não são PERMITIDAS!')
else:
    print('COMANDO INVALIDO!!!')
    exit()
sleep(1)
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    valor = 18 - idade
    print(f'Ainda falta {valor} anos para seu ALISTAMENTO!')
    anos =  ano_atual + valor
    print(f'O ano do seu alistamento é {anos}')
elif idade > 18:
    valor = idade - 18
    anos = ano_atual - valor
    print(f'Você já deveria ter se ALISTADO A {valor}')
    print(f'Deveria ter se alistado no a {anos}')'''

'''nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media} ')
    print('O aluno está APROVADO!')
elif media >= 5 and media < 7:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
    print('O aluno está em RECUPERAÇÃO!')
else:
    media < 5
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
    print('O aluno está REPROVADO')'''

'''from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('ANÇIÃO MASTER!!!')'''

'''peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sia altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc >= 18.5 and imc <= 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc >= 25 and imc <= 30:
    print('Você está em SOBREPESO')
elif imc >= 30 and imc <= 40:
    print('Voçê está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')'''

"""print(f"{'===== LOJAS MONMON =====':<40}")
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] á vista dinheiro/cheque
      [ 2 ] á vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão
      ''')"""

'''opção = int(input('Qual é a opção? '))

if opção == 1:
    desconto = (preço * 10) / 100
    comdescon = preço - desconto
    print(f'Sua compra de R${preço:.2f} vai custar R${comdescon:.2f} no final.')
elif opção == 2:
    desconto = (preço * 5) / 100
    condescon = preço - desconto
    print(f'Sua compra de R${preço:.2f} vai custar R${condescon:.2f} no final.')
elif opção == 3:
    parcela = preço / 2
    print(F'Sua compra de R${preço:.2f} em 2 vezes vai custar {parcela:.2f} reais SEM JUROS.') 
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        juros = preço * 20 / 100
        total = preço + juros
        valor_parcelas = total / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcelas:.2f} COM JUROS.')
        print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f}')
    if parcelas <= 2:
        print('O maximo é de 3x parcelas DESCULPE ')
else:
    print('OPÇÃO INVÁLIDA!')'''


"""from random import randint
itens = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
print('Suas opções: ')
print(''' 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
if jogador < 0 or jogador > 2:
    print('JOGADA INVÁLIDA ENCERRANDO o jogo!!!')
    exit()
print('-=' * 12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADO INVÁLIDA')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('COMANDO INVÁLIDO')
elif computador == 2: #Computador TESOURA
    if jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')"""




"""print(f"{'===== LOJAS DA RERE SASAKI =====':<40}")
preço = float(input('Preço das compras: R$'))
print(f"{'-=-=-=- FORMAS DE PAGAMENTO -=-=-=-':<40}")
print('''   
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão  
''')

opção = int(input('Qual é a opção? '))
if opção == 1:
    desconto = (preço * 10) / 100
    preço_final = preço - desconto
    print(f'Sua compra de R${preço:.2f} vai custar R${preço_final:.2f} no final.')
elif opção == 2:
    desconto = (preço * 5) / 100
    preço_final = preço - desconto
    print(f'Sua compra de R${preço:.2f} vai custar R${preço_final:.2f} no final.')
elif opção == 3:
    parcela = (preço / 2)
    print(f'Sua compra de R${preço:.2f} vai custar R${parcela} em 2 vezes SEM JUROS!')
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    if parcela >= 3:
        juros = (preço * 20) / 100
        juros_valor_final = preço + juros
        parcelas = juros_valor_final / parcela
        print(f'Sua compra está parcelada em {parcela}x de R${parcelas:.2f} COM JUROS.')
        print(f'Sua compra de R${preço} vai custar R${juros_valor_final:.2f} no FINAL.')
else:
    print('COMANDO INVÁLIDO!!!')"""

"""from time import sleep
from random import randint

computador = randint(0, 2)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('Suas opções:')
print('''
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA
''')

jogador = int(input('Qual é sua jogada? '))
print('JO')
print('KEN')
print('PO!!!')
sleep(1)
print('-=' * 13)
print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jogador]}')
print('-=' * 13)

if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador VENCE')
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('COMANDO INVÁLIDO')
if computador == 1: #PAPEL
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 0:
        print('Computador VENCE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('COMANDO INVÁLIDO')
elif computador == 2: #TESOURA
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    else:
        print('COMANDO INVÁLIDO')"""
    
'''for c in range( 0, 110, 10):
    print(c, end=' > ')
print('fim')'''


'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)'''

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

'''s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')'''


'''from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! BUM!')'''


'''for c in range(2, 51, 2):
    print(c, end=' ')
print('ACABOU!!!')'''

'''soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')'''

'''num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num *c }')'''


'''soma = 0
cont = 0
for c in range(1, 7):   
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')'''

'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 -1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end='> ')
print('ACABOU')'''

'''num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')'''

""""frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')"""

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
inverso = junto[::-1]
"""for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]"""
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')'''
'''from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')'''

'''peso_maior = 0
peso_menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f'O mair peso lido foi de {peso_maior}Kg')
print(f'O menor peso lido foi de {peso_menor}Kg')'''

'''maioridadehomem = 0
nome_velho = ''
idade_média = 0
totmenosde_vinte = 0
for p in range(1, 5):
    print(f'{p}° ----- PESSOA -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idade_média += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        totmenosde_vinte += 1
totidade_média = idade_média / 4
print(f'A média de idade do grupo é de {totidade_média} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nome_velho}')
print(f'Ao todo são {totmenosde_vinte} mulheres com menos de 20 anos')'''


'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1 
        else:
            impar += 1
print(f'Você digitou {par} números pares {impar} números ímpares!')'''

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')'''


"""from random import randint
computador = randint(0, 10)
print('''Sou um computador...
Acabei de pensar em um número entre 0 e 10,
Será que você consegue advinhar qual foi?''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print(f'Acertou com {palpites} tentativas. Parabéns!')"""

"""n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')"""

'''soma = num = cont = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')'''

'''resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números é a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')'''

'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')'''

'''n = 0
s = 0
cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma dos {cont} valores foi {s}')'''

from time import sleep
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
sleep(1)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')