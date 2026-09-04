# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

Projeto desenvolvido como parte do programa de iniciação em tecnologia. A ferramenta tem como objetivo auxiliar usuários no cálculo do consumo elétrico mensal de eletrodomésticos e equipamentos em geral, estimando também o impacto financeiro na conta de luz.

---

## 🚀 Funcionalidades

- 🔌 Cadastro rápido do aparelho por nome.
- ⚙️ Cálculo de consumo mensal baseado na potência ($W$) e tempo de uso diário ($h$).
- 💡 Conversão direta para quilowatts-hora ($kWh$).
- 💰 Estimativa de custo mensal baseada em tarifa padrão ($R\$\ 0{,}75/kWh$).

---

## 🧮 Fórmula Utilizada

O consumo elétrico mensal é determinado pela equação padrão:

$$\text{Consumo Mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Uso Diário (h)} \times 30}{1000}$$

O custo financeiro aproximado é obtido multiplicando o valor apurado pela tarifa:

$$\text{Custo Mensal (em reais)} = \text{Consumo Mensal (kWh)} \times 0{,}75$$

---

## 💻 Como Executar

### Pré-requisitos
- Ter o **Python 3.x** instalado na máquina.
- Git instalado (opcional, para clonar).

### Passo a passo

1. Clone o repositório ou faça o download dos arquivos:
```bash
   git clone https://github.com/Neytsinho/Projetos.git
```
2. Acesse a pasta do projeto: 
```bash  
   cd Projetos/consumo-energia
```   
3. Execute o programa:  
```bash  
   python app.py
```

