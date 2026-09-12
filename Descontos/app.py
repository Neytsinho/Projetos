# Programa de cálculo de descontos de uma loja online
# Autor: Natan

# Entrada
preco = float(input("Digite o preço total da compra: "))

# Processamento
if preco >= 300:
    desconto = preco * 0.15 
elif preco >= 200:
    desconto = preco * 0.10
else:  
    desconto = preco * 0.05

# Saída
print(f"O desconto aplicado é de R$ {desconto:.2f}")
print(f"O preço final da compra é de R$ {preco - desconto:.2f}")