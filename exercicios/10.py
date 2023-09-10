'''Crie uma classe chamada Lampada que representa uma lâmpada simples. A classe deve ter os seguintes atributos e métodos:

Atributos:

ligada (um valor booleano que representa se a lâmpada está ligada ou desligada).
Métodos:

Um método ligar que muda o valor do atributo ligada para True para indicar que a lâmpada está ligada.

Um método desligar que muda o valor do atributo ligada para False para indicar que a lâmpada está desligada.

Um método esta_ligada que retorna True se a lâmpada estiver ligada e False se estiver desligada.

Crie uma instância da classe Lampada, realize algumas operações de ligar e desligar e verifique se a lâmpada está ligada ou 
desligada em diferentes momentos.'''


class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada

    def ligar(self):
        if self.ligada == False:
            self.ligada = True
            print('Liguei a lâmpada')
        else:
            print('A lâmpada já está ligada')

    def desligar(self):
        if self.ligada == True:
            self.ligada = False
            print('Desliguei a lâmpada')
        else:
            print('A lâmpada já está desligada')

    # Getter:
    def get_ligada(self):
        print(f'A lâmpada está ligada: {self.ligada}')


lampada = Lampada(True)
lampada.get_ligada()
lampada.desligar()
lampada.desligar()
lampada.ligar()
lampada.get_ligada()
