#digite = input('Digite qualquer coisa: ')
#nome =  input('Digite o seu nome: ')
#idade = input('Digite sua idade: ')

#print(type(digite.isalnum()), nome.isalpha(), idade.isnumeric())

r =input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(r))
print('Só tem espaços? ', r.isspace())
print('É um número? ', r.isnumeric())
print('É alfabético? ', r.isalpha())
print('É alfanúmerico? ', r.isalnum())
print('Está em maiúsculas? ', r.isupper())
print('Está em minúsculas? ', r.islower())
print('Está capitalizada? ', r.istitle())