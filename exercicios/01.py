'''Crie uma classe chamada Animal que tenha os seguintes atributos e métodos:

Atributos:

nome - uma string que representa o nome do animal.
idade - um número inteiro que representa a idade do animal.
Métodos:

__init__ - O construtor da classe que inicializa os atributos nome e idade quando um objeto 
Animal é criado.
emitir_som - Um método que imprime uma mensagem simples, como "O animal faz um som."
Depois de criar a classe Animal, crie pelo menos dois objetos Animal com diferentes nomes e 
idades e chame o método emitir_som para cada um deles.'''


class Animal:
    def __init__(self, nome, idade, som):
        self.nome = nome
        self.idade = idade
        self.som = som

    def emite_som(self):
        return (f'Animal: {self.nome}\nSom: {self.som}')


animal1 = Animal('Cachorro', 5, 'auau')
animal2 = Animal('Gato', 3, 'miau')

print(animal1.emite_som())
print('-='*20)
print(animal2.emite_som())
