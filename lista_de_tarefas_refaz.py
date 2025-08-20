# Exercício - Lista de Tarefas com opções de desfazer e refazer

# todo = [] -> Lista de tarefas
# todo = ['fazer café'] -> Adicionar 'fazer café'
# todo = ['fazer café', 'caminhar'] -> Adicionar 'caminhar'

# desfazer = ['fazer café'] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']

# refazer = todo['fazer café']
# refazer = todo['fazer café', 'caminhar']

import os

# DECLARANDO AS VARIÁVEIS PRINCIPAIS
tarefas = [] # lista de tarefas principal para cadastro pelo usuário
tarefas_refazer = [] # lista de tarefas secundária, idêntica à principal, para uso posterior

# DEFINIÇÃO DAS FUNÇÕES DO EXERCÍCIO

# Limpeza do terminal
def clear_terminal():
    os.system('cls')

# Adição das tarefas à lista principal e à lista secundária
def adicionar_tarefa(tarefa):
    print()
    tarefas.append(tarefa)
    tarefas_refazer.append(tarefa)
    print('Tarefa adicionada!')
    print()

# Desfazer a última tarefa inserida
def desfazer(lista):
    lista.pop()

# Listagem das tarefas atuais registradas
def listar_tarefas():
    print()
    print('Lista de Tarefas:')
    for tarefa in tarefas:
        print (tarefa)
    print()

# CÓDIGO PRINCIPAL
while True:
    # Bloco de apresentação dos comandos ao usuário
    print('-=' * 30)
    print('Comandos Principais: LISTAR, DESFAZER, REFAZER')
    print('Comandos Opcionais: LIMPAR para limpar a tela ou SAIR para encerrar o programa')

    # Coleta do input do usuário
    user_input = input('Digite uma tarefa ou um dos comandos acima: ')
    user_task = user_input.lower()

    # Lógica do programa

    # Listagem das tarefas
    if user_task == 'listar':
        print()
        if not tarefas:
            print('Sem tarefas cadastradas!')
            print()
        else:
            listar_tarefas()
    # Desfazer última tarefa
    elif user_task == 'desfazer':
        print()
        if not tarefas:
            print('Não há tarefas a serem desfeitas!')
            print()
        else:
            desfazer(tarefas)
            print('Última tarefa desfeita!')
            listar_tarefas()
    # Refazer última tarefa
    elif user_task == 'refazer':
        print()
        if not tarefas:
            print('Não há tarefas a serem refeitas!')
            print()
        else:
            tarefas.append(tarefas_refazer.pop())
            print('Última tarefa digitada refeita!')
            listar_tarefas()
    # Limpeza da tela no terminal
    elif user_task == 'limpar':
        clear_terminal()
    # Encerramento do Programa
    elif user_task == 'sair':
        print()
        break
    # Adição da tarefa às listas
    else:
        adicionar_tarefa(user_input)
# Mensagem de encerramento
print('Programa FINALIZADO')