# 💧 Sistema de Monitoramento de Níveis de Reservatório de Água

Um script simples em Python que simula a medição periódica do nível de água em um reservatório e exibe avisos visuais no terminal com cores personalizadas usando a biblioteca [Colorama](https://pypi.org/project/colorama/).

---

## 📌 Funcionalidades

- **Simulação de Leitura:** Sorteia e analisa níveis de água em uma escala de 1 a 5.
- **Alertas Coloridos:** Formatação de texto no terminal para fácil identificação do status operacional.
- **Interatividade:** Permite que o usuário avance as leituras sob demanda pressionando a tecla `Enter`.

---

## 🎨 Tabela de Níveis e Alertas

| Nível | Status | Cor | Ação / Mensagem |
| :---: | :--- | :---: | :--- |
| **1** | Crítico | 🔴 Vermelho | Ação imediata necessária! |
| **2** | Baixo | 🟡 Amarelo | Verifique o reservatório. |
| **3** | Adequado | 🟢 Verde | Nenhuma ação necessária. |
| **4** | Alto | 🔵 Ciano | Monitoramento recomendado. |
| **5** | Muito Alto | 🟦 Azul | Risco de transbordamento! |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.6 ou superior instalado.
- Gerenciador de pacotes `pip`.

### 1. Clonar ou Baixar o Projeto

Salve o script em um arquivo, por exemplo: `monitor_reservatorio.py`.

### 2. Instalar Dependências

Instale a dependência necessária (`colorama`):

```bash
pip install colorama
```

### 3. Rodar o Script

Execute o comando no terminal:

```bash
python monitor_reservatorio.py
```

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** — Linguagem principal.
- **[Colorama](https://pypi.org/project/colorama/)** — Cores e estilos de texto no console.
- **`random`** — Módulo nativo do Python para geração das simulações.

---

## 📄 Licença

Este projeto é livre para estudos e melhorias. Sinta-se à vontade para adaptá-lo!