'''from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
 
if idade <= 9:
    print('O atleta tem {} anos.\n''Classificação: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos.\n''Classificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos.\n''Classificação: JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos.\n''Classificação: SÊNIOR'.format(idade))
else:
    print('O alteta tem {} anos.\n''Classificação: MASTER'.format(idade))'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[032mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[033mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[034mJÚNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[035mSÊNIOR\033[m')
else:
    print('Classificaçao: \033[031mMASTER!\033[m')

    
    


