'''Crie uma classe chamada Ponto2D que represente um ponto no plano cartesiano com coordenadas x e y. A classe deve ter os 
seguintes atributos e métodos:

Atributos:

x - um número decimal que representa a coordenada x do ponto.
y - um número decimal que representa a coordenada y do ponto.
Métodos:

__init__ - O construtor da classe que inicializa os atributos x e y quando um objeto Ponto2D é criado.
mover - Um método que aceita novas coordenadas x e y como entrada e move o ponto para essas coordenadas.
calcular_distancia - Um método que aceita outro objeto Ponto2D como entrada e calcula a distância entre os dois pontos usando a 
fórmula da distância euclidiana: √((x2 - x1)² + (y2 - y1)²).
exibir_coordenadas - Um método que exibe as coordenadas atuais do ponto no formato "(x, y)".
Depois de criar a classe Ponto2D, crie dois objetos Ponto2D, realize operações de movimento, calcule a distância entre eles e exiba
 suas coordenadas.'''


class Ponto2D:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def mover(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def calcula_distancia(self, outro_ponto):
        return f'{(((self.x - outro_ponto.x)**2) + ((self.y - outro_ponto.y)**2))**0.5:.2f}'

    def exibir_coordenadas(self):
        return (f'X={self.x}, Y={self.y}')


ponto1 = Ponto2D(1, 2)
ponto2 = Ponto2D(4, 6)

ponto1.mover(3, 5)

print(f'Ponto1 = {ponto1.exibir_coordenadas()}')
print(f'Ponto2 = {ponto2.exibir_coordenadas()}')

print(f'Distância: {ponto1.calcula_distancia(ponto2)}')
