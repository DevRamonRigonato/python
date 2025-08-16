import random

def escolher_palavra_por_dificuldade():
    # Uma lista maior de palavras
    palavras = [
        "casa", "bola", "sol", "peixe", "flor",  # curtas
        "janela", "telefone", "computador", "cozinha", "montanha", # médias
        "bicicleta", "hipopotamo", "desenvolvimento", "programacao", "inteligencia" # longas
    ]

    print("Escolha o nível de dificuldade:")
    print("(1) Fácil - Palavras de 3 a 5 letras")
    print("(2) Médio - Palavras de 6 a 9 letras")
    print("(3) Difícil - Palavras com 10 ou mais letras")

    while True:
        try:
            nivel = int(input("Digite o número do nível (1, 2, ou 3): "))
            if nivel in [1, 2, 3]:
                break
            else:
                print("Escolha um número válido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    palavras_filtradas = []

    if nivel == 1:
        # Filtra palavras fáceis
        palavras_filtradas = [p for p in palavras if 3 <= len(p) <= 5]
    elif nivel == 2:
        # Filtra palavras médias
        palavras_filtradas = [p for p in palavras if 6 <= len(p) <= 9]
    elif nivel == 3:
        # Filtra palavras difíceis
        palavras_filtradas = [p for p in palavras if len(p) >= 10]
    
    # Se a lista filtrada estiver vazia, avisa o usuário
    if not palavras_filtradas:
        print("Não há palavras disponíveis para este nível. Escolhendo uma palavra aleatória.")
        return random.choice(palavras)
    
    # Sorteia uma palavra da lista filtrada
    return random.choice(palavras_filtradas)

# Exemplo de como usar a função no seu jogo principal:
# palavra_secreta = escolher_palavra_por_dificuldade().lower()
# print(f"A palavra escolhida para o jogo tem {len(palavra_secreta)} letras.")