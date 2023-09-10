'''Metodos de classes'''

from datetime import date


class Pessoa:
    ano_atual = date.today().year

    def __init__(self, nome, idade,comer=False, falar=False):
        self.nome = nome
        self.idade = idade
        self.comer = comer
        self.falar = falar


    def get_ano_nascimento(self):
        print(f'Ano de nascimento: {self.ano_atual - self.idade}')

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa.por_ano_nascimento('Diego', 2005)
p1.get_ano_nascimento()

print(p1.idade)
print(p1.numero)
