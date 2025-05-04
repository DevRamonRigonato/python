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
















