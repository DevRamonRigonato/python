r =(input('Digite algo: '))

print('O tipo primitivo desse valor é {}'.format(type(r)))
print('Só tem espaços? {}'.format (r.isspace()))
print('É um número? {}'.format(r.isnumeric()))
print('É alfabético? {}'.format(r.isalpha()))
print('É alfanúmerico? {}'.format(r.isalnum()))
print('Está em maiúsculas? {}'.format(r.isupper()))
print('Está em minúsculas? {}'.format(r.islower()))
print('Está capitalizada? {}'.format(r.istitle()))
