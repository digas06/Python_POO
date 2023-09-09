'''Classe de Livro:
Crie uma classe chamada Livro que represente informações sobre um livro, como título, autor e número de páginas. 
Crie métodos para calcular o número de palavras com base no número de páginas (supondo uma média de 250 palavras por página)
 e para exibir informações sobre o livro.'''


class Livro:
    def __init__(self, titulo='', autor='', numero_paginas=0):
        self.tiulo = titulo
        self.autor = autor
        self.numero_paginas = int(numero_paginas)

    def calcula_palavra(self):
        return f'+/-: {self.numero_paginas * 250}'

    def informacoes(self):
        print(f'{"~"*40}\n{"Informações": ^40}\n{"~"*40}')
        titulo = print(f'{"Título:":_<15}{self.tiulo: <15}')
        aultor = print(f'{"Autor:":_<20}{self.autor:_>20}')
        paginas = print(f'{"Páginas:":_<20}{self.numero_paginas:_>20}')
        palavras = print(
            f'{"palavras":_<20}{self.calcula_palavra():_>20}\n{"~"*40}')


l1 = Livro('A volta dos que não foram', 'Diego', 20)

l1.informacoes()
