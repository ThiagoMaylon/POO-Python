'''
    classe
    objeto
    contrutor
    metodos
    atributos
    herança

    sobrecarga de metodos
    polimofismo
    destrutores
'''

class Pessoa(object): # classe pessoa
    nome = 'João' # Atributo nome


class Casa(object):
    cor = 'Amarela'
    quartos = 5

obj = Pessoa() # objeto que recebe a classe pessoa


minha_casa = Casa()
print(f"Minha casa é {minha_casa.cor} e tem {minha_casa.quartos} quartos")