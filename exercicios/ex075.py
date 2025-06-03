cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    núm = int(input('Digite um número entre: [0 e 20] '))
    if 0 <= núm <= 20: # verificar se um número está dentro de um intervalo / Se 0 é menor ou igual a núm e núm é menor ou igual a 20
        print(f'O número é {cont[núm]}')
        break
resp = ''
while True:
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('Encerrando programa até logo')
        break
    while True:
        núm = int(input('Digite um número entre: [0 e 20] '))
        if 0 <= núm <= 20: # verificar se um número está dentro de um intervalo / Se 0 é menor ou igual a núm e núm é menor ou igual a 20
            print(f'O número é {cont[núm]}')
            break
