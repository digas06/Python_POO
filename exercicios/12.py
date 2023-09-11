'''Crie uma classe chamada Produto que represente produtos em um sistema de controle de estoque. A classe deve ter os seguintes 
atributos:

codigo (um número inteiro único que identifica o produto).
nome (uma string que representa o nome do produto).
quantidade (um número inteiro que representa a quantidade em estoque).
preco (um número decimal que representa o preço do produto).
A classe Produto deve ter os seguintes métodos:

Um método __init__ que inicializa os atributos do produto quando um objeto é criado.

Um método de classe chamado alterar_preco que permite que você altere o preço de um produto com base em seu código.

Um método de classe chamado adicionar_estoque que recebe um valor inteiro e adiciona essa quantidade ao estoque do produto.

Um método de classe chamado vender que recebe um valor inteiro e subtrai essa quantidade do estoque do produto, desde que a 
quantidade em estoque seja suficiente. Se não houver estoque suficiente, deve ser exibida uma mensagem informando que não é possível 
concluir a venda.

Um método de classe chamado calcular_valor_total que retorna o valor total em estoque multiplicando a quantidade pelo preço.

Crie instâncias da classe Produto, realize operações de adição ao estoque, venda, alteração de preço e calcule o valor total em 
estoque.'''


class Produto:
    lista_de_produtos = {}

    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        Produto.lista_de_produtos[codigo] = [nome, quantidade, preco]

    @classmethod
    def alterar_preco(cls, codigo, novo_valor):
        if codigo in cls.lista_de_produtos:
            cls.lista_de_produtos[codigo][2] = novo_valor
        else:
            print('Produto inezistente!')

    @classmethod
    def adicionar_estoque(cls, codigo, quantidade):
        if codigo in cls.lista_de_produtos:
            cls.lista_de_produtos[codigo][1] += quantidade
        else:
            print('Produto inezistente!')

    @classmethod
    def vender(cls, codigo, quantidade):
        if codigo in cls.lista_de_produtos:
            if cls.lista_de_produtos[codigo][1] >= quantidade:
                cls.lista_de_produtos[codigo][1] -= quantidade
                print(f'Venda concluída.')
            else:
                print('Não possui estoque suficiente!')
        else:
            print('Produto inezistente!')

    @classmethod
    def calcular_valor_total(cls, codigo):
        if codigo in cls.lista_de_produtos:
            return cls.lista_de_produtos[codigo][2] * cls.lista_de_produtos[codigo][1]


produto1 = Produto(1, "Camiseta", 10, 25.0)
produto2 = Produto(2, "Calça Jeans", 5, 50.0)

Produto.alterar_preco(2, 45.0)

Produto.adicionar_estoque(1, 5)

Produto.vender(1, 3)
Produto.vender(2, 7)

valor_total = Produto.calcular_valor_total(1)
print(f"Valor total em estoque do produto 1: R${valor_total:.2f}")
