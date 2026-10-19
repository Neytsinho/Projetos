"""
Sistema de Monitoramento de Níveis de Reservatório de Água.
Exibe alertas coloridos no terminal com base no nível da água utilizando Colorama.
"""

import random
from colorama import Fore, Style

# Lista contendo as definições dos níveis do reservatório
nivels = [1, 2, 3, 4, 5]

def verificar_nivel():
    """
    Função para simular a verificação do nível de água no reservatório.
    Retorna um nível aleatório entre 1 e 5.
    """
    return random.choice(nivels)
def cor(nivel):
    """Função para determinar a cor do alerta com base no nível de água.
    Retorna a cor correspondente ao nível."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


def exibir_alerta(nivel):
    """Função para exibir o alerta correspondente ao nível de água.
    Recebe o nível de água como parâmetro e imprime a mensagem de alerta com a cor apropriada."""
    if nivel == 1:
        print(f"{cor(nivel)}ALERTA: Nível crítico de água! Ação imediata necessária!{Style.RESET_ALL}")
    elif nivel == 2:
        print(f"{cor(nivel)}AVISO: Nível baixo de água. Verifique o reservatório.{Style.RESET_ALL}")
    elif nivel == 3:
        print(f"{cor(nivel)}Nível de água adequado. Nenhuma ação necessária.{Style.RESET_ALL}")
    elif nivel == 4:
        print(f"{cor(nivel)}Nível de água acima do normal. Monitoramento recomendado.{Style.RESET_ALL}")
    elif nivel == 5:
        print(f"{cor(nivel)}Nível de água muito alto! Risco de transbordamento!{Style.RESET_ALL}")
    else:
        print(f"{cor(nivel)}Nível de água desconhecido. Verifique o sistema.{Style.RESET_ALL}")

def simular_monitoramento():
    """
    Função principal para simular o monitoramento do nível de água no reservatório.
    Verifica o nível e exibe o alerta correspondente.
    """
    nivel_atual = verificar_nivel()
    exibir_alerta(nivel_atual)

while True:
    '''
    Loop principal para simular o monitoramento do nível de água no reservatório.
    '''
    simular_monitoramento()
    input("Pressione Enter para verificar novamente...")