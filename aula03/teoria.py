'''Metodos estáticos'''
from datetime import date
from random import randint


class Pessoa:
    ano_atual = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(f'Nascimento: {Pessoa.ano_atual - self.idade}')

    @classmethod
    def idade_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def cria_id():
        id = randint(10000, 99999)
        return id


p1 = Pessoa.idade_por_ano_nascimento('Diego', 2005)
print(p1.cria_id())
