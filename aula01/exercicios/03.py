'''Crie uma classe chamada ContaBancaria que tenha os seguintes atributos e métodos:

Atributos:

numero_conta - um número inteiro que representa o número da conta bancária.
saldo - um valor decimal que representa o saldo disponível na conta bancária.

Métodos:

__init__ - O construtor da classe que inicializa os atributos numero_conta e saldo quando um objeto 
ContaBancaria é criado.
depositar - Um método que aceita um valor como entrada e adiciona esse valor ao saldo da conta bancária.
sacar - Um método que aceita um valor como entrada e subtrai esse valor do saldo da conta bancária, 
desde que haja saldo suficiente. Caso contrário, exibe uma mensagem informando que não há saldo suficiente.
consultar_saldo - Um método que retorna o saldo atual da conta bancária.
Depois de criar a classe ContaBancaria, crie um objeto ContaBancaria, realize algumas operações 
de depósito e saque e consulte o saldo para verificar as funcionalidades.'''


class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = int(numero_conta)
        self.saldo = float(saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')

    def consulta_saldo(self):
        print(f'saldo atual: {self.saldo:.2f}')


conta = ContaBancaria(1234, 5000)

conta.consulta_saldo()
conta.depositar(10)
conta.consulta_saldo()
conta.sacar(5010.50)
