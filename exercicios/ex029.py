print('-=-' * 20)
print('\033[0;36mAnalisador de Triângulos\033[0m') 
print('-=-' * 20)      
r1 = float(input('\033[0;33mPrimeiro segmento:\033[0m '))   
r2 = float(input('\033[0;33mSegundo segmento: \033[0m'))     
r3 = float(input('\033[0;33mTerceiro segmento: \033[0m'))    

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;32mOs seguimentos acima PODEM FORMAR triângulo!\033[0m')
else:
    print('\033[0;31mOs segmentos acima NÃO PODEM formar triângulo!\033[0m')

 
