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

class ContaBancaria(object):
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        self.ver_saldo()
    
    def sacar(self, valor):
        self.saldo -= valor
        self.ver_saldo()
    
    def ver_saldo(self):
        print(f"seu Saldo é de {self.saldo:.2f}")

class ContaPoupanca(ContaBancaria): # herda método e atributos da classe ContaBancaria
    def _consulta_rentabilidade(self): # método privado
        return 1.6
    
    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if(rentabilidade < 0.5):
            print('consulte o seu gerente')
        else:
            print(rentabilidade)

conta_poupanca = ContaPoupanca()
conta_poupanca.rentabilidade()
conta_poupanca.depositar(100)
conta_poupanca.sacar(45.50)