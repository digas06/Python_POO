'''Crie uma classe chamada Carro que tenha os seguintes atributos e métodos:

Atributos:

marca - uma string que representa a marca do carro.
modelo - uma string que representa o modelo do carro.
ano - um número inteiro que representa o ano de fabricação do carro.

Métodos:

__init__ - O construtor da classe que inicializa os atributos marca, modelo e ano quando um 
objeto Carro é criado.
get_informacoes - Um método que retorna uma string contendo as informações completas do carro, 
como "Marca: [marca], Modelo: [modelo], Ano: [ano]."
Depois de criar a classe Carro, crie pelo menos um objeto Carro com valores específicos para 
os atributos e chame o método get_informacoes para exibir as informações do carro.'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def get_informacoes(self):
        return (f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}')
    
carro1 = Carro('Fiat', 'Toro', 2011)
carro2 = Carro('Honda', 'Civc', 2010)

print(carro1.get_informacoes())
print('-='*20)
print(carro2.get_informacoes())