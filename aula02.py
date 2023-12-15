'''
    classe
    objeto
    contrutor
    métodos
    atributos
    herança

    sobrecarga de metodos
    polimofismo
    destrutores
'''

class Casa(object):
    cor = "Amarela"
    quartos = 3

    def __init__(self, cor, quartos): # método contrutor
        self.cor = cor
        self.quartos = quartos

    def pintar(self, cor): # método de pintar a casa
        self.cor = cor
    def aumenta_quartos(self, quartos):
        self.quartos = quartos
        

minha_casa = Casa('Vermelha', 3)

print(f'Minha casa é {minha_casa.cor} e tem {minha_casa.quartos} quartos')
minha_casa.pintar('Roxa')
minha_casa.aumenta_quartos(5)
print(f"Agora a minha Casa é {minha_casa.cor} e tem {minha_casa.quartos} quartos")