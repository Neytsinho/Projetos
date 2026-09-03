# Programa de cálculo de consumo elétrico
# Autor: Natan
# Entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia do aparelho em watts(W): "))
tempo = float(input("Digite o tempo de uso diario em horas: "))
# Processamento
consumo = (potencia * tempo * 30) / 1000  # Convertendo para kWh
custo = consumo * 0.75  # Considerando o custo de R$ 0,75 por kWh
# Saída
print(f"\nAparelho: {aparelho}")
print(f"Consumo: {consumo:.2f} kWh")
print(f"Custo mensal: R$ {custo:.2f}")