'''n1 = (int(input('Primeiro valor: ')))
n2 = (int(input('Segundo valor: ')))
n3 = (int(input('Terceiro valor: ')))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
        menor = n3

if n1 > n2 and n1 > n3:
     maior = n1   
if n2 > n3 and n2 > n1:
     maior = n2
if n3 > n1 and n3 > n2:
     maior = n3

print('Número maior {}'.format(maior))
print('Número menor: {}'.format(menor))'''  


n1 = (int(input('Primeiro valor: ')))
n2 = (int(input('Segundo valor: ')))
n3 = (int(input('Terceiro valor: ')))

#Verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))