'''Crie uma classe chamada Calculadora que possui um método estático chamado calcular_media. O método estático deve receber 
uma lista de números e calcular a média desses números. A classe Calculadora não deve ter atributos de instância, apenas o método 
estático.

Você pode começar definindo a classe Calculadora e implementando o método estático calcular_media dentro dela. 
O método calcular_media deve aceitar uma lista de números como argumento e retornar a média desses números.'''

class Calculadora:
    def calcula_media(lista):
        soma = sum(lista)
        return soma / len(lista)
    
lista = [1,3,10,2]
print(f'Média da lista: {Calculadora.calcula_media(lista)}')
