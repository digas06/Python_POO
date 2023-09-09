'''Crie uma classe chamada AgendaContatos que permita armazenar e gerenciar uma lista de contatos. A classe deve ter os 
seguintes métodos:

Métodos:

__init__ - O construtor da classe que inicializa uma lista vazia de contatos quando um objeto AgendaContatos é criado.
adicionar_contato - Um método que aceita o nome e o número de telefone de um contato como entrada e adiciona esse contato à 
lista de contatos.
remover_contato - Um método que aceita o nome de um contato como entrada e remove esse contato da lista de contatos, se ele existir.
listar_contatos - Um método que lista todos os contatos na agenda.
buscar_contato - Um método que aceita o nome de um contato como entrada e retorna o número de telefone desse contato, se ele existir,
 ou exibe uma mensagem informando que o contato não foi encontrado.
Depois de criar a classe AgendaContatos, crie um objeto AgendaContatos, adicione alguns contatos, liste-os, busque por um contato e 
remova um contato.'''


class AgendaContatos:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, numero):
        self.contatos[nome] = numero

    def remover_contato(self, nome):
        try:
            del self.contatos[nome]
        except:
            print('O contato não existe')

    def listar_contatos(self):
        print(f'{"="*30}\n{"Nome:": <15}{"Número:": <15}\n{"="*30}')

        for nome, numero in self.contatos.items():
            print(f'{nome: <15}{numero: <15}')
        print('='*30)

    def buscar_contato(self, nome):
        for c in self.contatos.keys():
            if c == nome:
                return (f'{c}:  {self.contatos[nome]}')

            else:
                print('\033[31mContato não encontrado!\033[0m')
                break


agenda = AgendaContatos()

agenda.adicionar_contato('Diego', 985360715)
agenda.adicionar_contato('Luiz', 986189608)
agenda.adicionar_contato('Ester', 996710353)
agenda.listar_contatos()
print(f'Telefone de {agenda.buscar_contato("Diego")}')
agenda.remover_contato('Ester')
print()
print('Lista de contato após remoção:')
agenda.listar_contatos()
