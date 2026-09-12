# Programa para classificar o perfil de consumo dos imóveis
# Autor: Natan

# Entrada
tipo = input("Digite o tipo de imóvel (1 - comercial, 2 - residencial(casa ou apartamento)): ")
Consumo = int(input("Digite o consumo de água (m³): "))

# Processamento E saída
match tipo:
    case "1":
        print("Tarifa comercial aplicada – consulte o plano corporativo")
    case "2":
        if Consumo > 25:
            print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
        elif Consumo <= 25 and Consumo >= 10:
            print("Consumo moderado – dentro do padrão residencial.")
        else:
            print("Consumo baixo – ótimo aproveitamento de recursos.")
    case _:
        print("Tipo de imóvel inválido. Por favor, insira 1 para comercial ou 2 para residencial.")


