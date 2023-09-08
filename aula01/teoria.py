from datetime import date


class Pessoa:
    ano_atual = date.today().year
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def ano_nascimento(self):
        return self.ano_atual - self.idade

    def falar(self, assunto):
        if self.comendo:
            return (f'{self.nome} não pode falar comendo.')
        if self.falando:
            return (f'{self.nome} já está falando.')
        else:
            self.falando = True
            return (f'{self.nome} está falando sobre {assunto}')

    def parar_falar(self):
        if self.falando:
            self.falando = False
            return (f'{self.nome} parou de falar.')
        else:
            return (f'{self.nome} não está falando.')

    def comer(self, alimento):
        if self.falando:
            return(f'{self.nome} não pode comer enquanto fala.')
        if not self.comendo:
            self.comendo = True
            return (f'{self.nome} está comendo {alimento}')
        else:
            return (f'{self.nome} já está comendo.')

    def parar_comer(self):
        if self.comendo:
            self.comendo = False
            return (f'{self.nome} parou de comer')
        else:
            return (f'{self.nome} não está comendo.')

