# Programa para Pesquisa de Satisfação - TudoWeb
# Autor: Natan

# Inicialização dos contadores
total_excelente = 0
total_bom = 0
total_ruim = 0

# Quantidade total de entrevistados
total_entrevistados = 10

print("=== Pesquisa de Satisfação - TudoWeb ===")

# Estrutura de repetição
for i in range(1,total_entrevistados + 1): 
    print(f"\nEntrevistado {i}:")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    print("Avalie nosso serviço:")
    print("1 - Excelente | 2 - Bom | 3 - Ruim")

    avaliacao = input("Digite sua avaliação (1, 2 ou 3): ")

    # Estrutura de decisão para verificar a opinião
    match avaliacao:
        case "1":
            total_excelente += 1
        case "2":
            total_bom += 1
        case "3":
            total_ruim += 1
        case _:
            print("Avaliação inválida. Por favor, insira 1, 2 ou 3.")

# Exibição dos resultados finais
print("\n=== Resultados da Pesquisa ===")
print(f"Excelente: {total_excelente}")
print(f"Bom: {total_bom}")
print(f"Ruim: {total_ruim}")