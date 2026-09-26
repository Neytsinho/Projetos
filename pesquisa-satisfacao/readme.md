# Pesquisa de Satisfação - TudoWeb 📊

Script em Python desenvolvido para coletar e tabular avaliações de atendimento de clientes da empresa **TudoWeb** via linha de comando.

---

## 📌 Sobre o Projeto

O programa realiza uma pesquisa com uma quantidade fixa de entrevistados (configurada por padrão para 10 pessoas). Durante a execução, ele solicita os dados de identificação e a nota atribuída ao serviço, consolidando o total de cada classificação ao final.

### ✨ Funcionalidades

- **Coleta de dados:** Registro do nome e da idade de cada participante.
- **Menu de avaliação:**
  - `1` - Excelente
  - `2` - Bom
  - `3` - Ruim
- **Tratamento de entrada:** Alerta o usuário caso seja digitada uma opção inválida.
- **Relatório final:** Apresentação da contagem consolidada das respostas.

---

## 🛠️ Tecnologias e Requisitos

- **Linguagem:** Python 3.10 ou superior *(obrigatório devido ao uso da sintaxe `match/case`)*.
- **Dependências externas:** Nenhuma (utiliza apenas a biblioteca padrão).

---

## 🚀 Como Executar

### 1. Pré-requisitos

Verifique se você possui o Python 3.10+ instalado no seu sistema:

```bash
python --version
# ou
python3 --version
```

### 2. Executando o script

1. Baixe ou salve o código em um arquivo chamado `pesquisa.py`.
2. Abra o terminal no mesmo diretório do arquivo e execute:

```bash
python pesquisa.py
# ou
python3 pesquisa.py
```

---

## 💻 Exemplo de Execução

```text
=== Pesquisa de Satisfação - TudoWeb ===

Entrevistado 1:
Digite seu nome: Carlos
Digite sua idade: 28
Avalie nosso serviço:
1 - Excelente | 2 - Bom | 3 - Ruim
Digite sua avaliação (1, 2 ou 3): 1

Entrevistado 2:
...

=== Resultados da Pesquisa ===
Excelente: 7
Bom: 2
Ruim: 1
```

---

## 👤 Autor

Desenvolvido por **Natan**.