'''Crie uma classe chamada Produto que permita representar informações sobre produtos. A classe deve ter os seguintes atributos 
e métodos:

Atributos:

nome - uma string que representa o nome do produto.
preco - um valor decimal que representa o preço do produto.
estoque - um número inteiro que representa a quantidade em estoque do produto.
Métodos:

__init__ - O construtor da classe que inicializa os atributos nome, preco e estoque quando um objeto Produto é criado.
adicionar_estoque - Um método que aceita um valor como entrada e adiciona essa quantidade ao estoque do produto.
remover_estoque - Um método que aceita um valor como entrada e remove essa quantidade do estoque do produto, desde que haja estoque 
suficiente. Caso contrário, exibe uma mensagem informando que não há estoque suficiente.
calcular_valor_total - Um método que calcula o valor total do estoque do produto multiplicando o preço pelo estoque disponível.
exibir_informacoes - Um método que exibe todas as informações do produto, incluindo nome, preço e estoque.
Depois de criar a classe Produto, crie um objeto Produto, realize operações de adição e remoção de estoque, calcule o valor total do
 estoque e exiba as informações do produto.'''

class Produto:
    def __init__(self, nome, preco=0, estoque=0):
        self.nome = nome
        self.preco = float(preco)
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
        else:
            print('Não há estoque suficiente.')

    def calcular_valor_total(self):
        return (f'Valor total: R$ {self.estoque*self.preco:.2f}')
    
    def exibir_informacoes(self):
        print(f'Nome: {self.nome}\nPreço: R$ {self.preco:.2f}\nEstoque: {self.estoque}')


produto = Produto('Arroz', 20)

produto.adicionar_estoque(20)
produto.remover_estoque(5)
print(f'{produto.calcular_valor_total()}')
produto.exibir_informacoes()
