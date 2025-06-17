lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    # Se for o primeiro valor ou maior que o último da lista, adiciona no final
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        # Procura a posição certa para inserir
        while pos < len(lista): # Ele vai da posição 0 até a última posição
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break # Sai do while após inserir
            pos += 1 # Vai pra próxima posição
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
