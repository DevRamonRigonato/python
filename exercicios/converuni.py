def metros_para_quilometros(metros: float) -> float:
    return metros / 1000


def quilometros_para_metros(quilometros: float) -> float:
    return quilometros * 1000


def quilometros_para_milhas(quilometros: float) -> float:
    return quilometros * 0.621371


def milhas_para_quilometros(milhas: float) -> float:
    return milhas / 0.621371


def celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9


# --- Conversões de área ---
def hectares_para_m2(hectares: float) -> float:
    return hectares * 10_000


def m2_para_hectares(m2: float) -> float:
    return m2 / 10_000


def acres_para_m2(acres: float) -> float:
    return acres * 4046.86


def m2_para_acres(m2: float) -> float:
    return m2 / 4046.86


def menu():
    print("\n=== Conversor de Unidades ===")
    print("1. Metros -> Quilômetros")
    print("2. Quilômetros -> Metros")
    print("3. Quilômetros -> Milhas")
    print("4. Milhas -> Quilômetros")
    print("5. Celsius -> Fahrenheit")
    print("6. Fahrenheit -> Celsius")
    print("7. Hectares -> m²")
    print("8. m² -> Hectares")
    print("9. Acres -> m²")
    print("10. m² -> Acres")
    print("0. Sair")


def main():
    while True:
        menu()
        escolha = input("Escolha a conversão: ")

        if escolha == "0":
            print("Saindo... Até logo!")
            break

        try:
            valor = float(input("Digite o valor a ser convertido: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        if escolha == "1":
            print(f"{valor} metros = {metros_para_quilometros(valor):.2f} km")
        elif escolha == "2":
            print(f"{valor} km = {quilometros_para_metros(valor):.2f} m")
        elif escolha == "3":
            print(f"{valor} km = {quilometros_para_milhas(valor):.2f} mi")
        elif escolha == "4":
            print(f"{valor} mi = {milhas_para_quilometros(valor):.2f} km")
        elif escolha == "5":
            print(f"{valor} °C = {celsius_para_fahrenheit(valor):.2f} °F")
        elif escolha == "6":
            print(f"{valor} °F = {fahrenheit_para_celsius(valor):.2f} °C")
        elif escolha == "7":
            print(f"{valor} hectares = {hectares_para_m2(valor):.2f} m²")
        elif escolha == "8":
            print(f"{valor} m² = {m2_para_hectares(valor):.4f} hectares")
        elif escolha == "9":
            print(f"{valor} acres = {acres_para_m2(valor):.2f} m²")
        elif escolha == "10":
            print(f"{valor} m² = {m2_para_acres(valor):.4f} acres")
        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    main()
