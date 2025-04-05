from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nascimento = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('\033[0;32mAo todo tivemos {} pessoas maiores de idade\033[m'.format(totmaior))
print('\033[0;32mE também tivemos {} pessoas menores de idade\033[m'.format(totmenor))

