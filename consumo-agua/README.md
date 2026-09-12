# 💧 Classificador de Perfil de Consumo Hídrico

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![License](https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge)
![Water Sustainability](https://img.shields.io/badge/Sustentabilidade-Recursos%20Hídricos-0077be?style=for-the-badge&logo=airplay&logoColor=white)

---

## 📌 Sobre o Projeto

O **Classificador de Perfil de Consumo de Imóveis** é um script desenvolvido em **Python** com o objetivo de analisar e categorizar o volume de consumo mensal de água ($m^3$) de diferentes tipos de imóveis (comerciais e residenciais).

O sistema auxilia na identificação de perfis de consumo, orientando o usuário sobre tarifas corporativas aplicadas ou sugerindo medidas de sustentabilidade e detecção de vazamentos.

---

## ⚙️ Regras de Negócio e Classificação

O processamento é feito com base no tipo de imóvel informado:

### 🏢 1. Imóvel Comercial
* Aplica orientação sobre a tarifa comercial e sugere consulta ao plano corporativo.

### 🏠 2. Imóvel Residencial (Casa ou Apartamento)
O perfil é classificado a partir do consumo em $m^3$:
| Faixa de Consumo ($m^3$) | Classificação | Feedback ao Usuário |
| :--- | :--- | :--- |
| **Maior que 25** | Consumo Excessivo | ⚠️ Adote medidas de economia e verifique vazamentos. |
| **Entre 10 e 25** | Consumo Moderado | ✅ Dentro do padrão residencial. |
| **Menor que 10** | Consumo Baixo | 💧 Ótimo aproveitamento de recursos. |

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** [Python 3.10+](https://www.python.org/) *(uso da estrutura `match-case`)*
* **Paradigma:** Estruturado / CLI (Interface de Linha de Comando)

---

## 💻 Como Executar

### Pré-requisitos
* Ter o Python instalado (versão **3.10 ou superior**, necessária para a sintaxe `match/case`).

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Neytsinho/Projetos.git
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd Projetos/consumo-agua
   ```

3. **Execute o programa:**
   ```bash
   python main.py
   ```

4. **Siga as instruções no terminal:**
   * Informe o tipo de imóvel (`1` para comercial ou `2` para residencial).
   * Digite o consumo mensal de água em $m^3$.

---

## 👨‍💻 Autor

Desenvolvido por **Natan**.

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)