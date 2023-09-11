'''Crie uma classe chamada ListaDeTarefas que representa uma lista de tarefas. A classe deve ter os seguintes atributos e métodos:

Atributos:

tarefas (uma lista que armazena as tarefas).
Métodos:

Um método adicionar_tarefa que recebe uma tarefa como argumento e a adiciona à lista de tarefas.

Um método remover_tarefa que recebe o índice de uma tarefa na lista e a remove.

Um método listar_tarefas que imprime todas as tarefas da lista.

Crie uma instância da classe ListaDeTarefas e realize operações de adição, remoção e listagem de tarefas.'''
from time import sleep


class ListaDeTarefas:
    tarefas = []

    def adicionar_tarefas(cls, tarefa):
        cls.tarefas.append(tarefa)
        sleep(1)
        print(f'\033[32mTarefa adicionada!\033[0m')

    def remover_tarefa(cls, posicao):

        print(f'\033[32m\"{cls.tarefas[posicao]}\" removido da lista\033[0m')
        del cls.tarefas[posicao]
        sleep(1)

    def listar_tarefas(cls):
        if len(cls.tarefas) > 0:
            print(f'\033[33m{"ID": <10}\033[0m{"tarefa":<15}\n{"_"*20}')
            for pos, c in enumerate(cls.tarefas):
                print(f'\033[33m{pos:.<10}\033[0m{c:<}')
                sleep(0.5)
        else:
            print(f'{"-"*30}\033[31mSua lista está vazia!\033[0m{"-"*30}')
            sleep(1)


lista = ListaDeTarefas()

print(f'\033[33mBem vindo a sua lista de tarefas.\033[0m')

while True:
    print(f'''{"-="*20}
\033[32m[ 1 ] Adicionar tarefa.
[ 2 ] Remover tarefa.
[ 3 ] Ver lista.
[ Ctrl + c ] Parar programa\033[0m\n{"-="*20}''')

    try:
        escolha = int(input('O que deseja fazer? '))

        if escolha == 1:
            try:
                lista.adicionar_tarefas(input('Tarefa: '))
                sleep(1.5)

            except:
                print('\033[31mVocê não pode adicionar isso a lista!\033[0m')
                sleep(1.5)

        elif escolha == 2:
            try:
                lista.remover_tarefa(int(input('Posição da tarefa: ')))
                sleep(1.5)
            except:
                print(
                    f'{"-"*20}\033[31mAlgo deu errado. Digite uma posição válida.\033[0m{"-"*20}')
                sleep(1.5)

        elif escolha == 3:
            lista.listar_tarefas()
            sleep(1)

        else:
            print('\033[31mEssa opção é inválida\033[0m')
            sleep(2)

    except KeyboardInterrupt:
        break
    except:
        print('\033[31mOpção inválida. tente novamente.\033[0m')
        sleep(2)
