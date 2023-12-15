'''
    overrride de métodos
    polimofismo
    destrutores
'''

class ContaBancaria(object):
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        print('depositar da Super classe')
        self.saldo += valor
        self.ver_saldo()
    
    def sacar(self, valor):
        self.saldo -= valor
        self.ver_saldo()
    
    def ver_saldo(self):
        print(f"seu Saldo é de {self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
    rentabilidade_total = 1.6
    def _consulta_rentabilidade(self): # método privado
        return self.rentabilidade_total
    
    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if(rentabilidade < 0.5):
            print('consulte o seu gerente')
        else:
            print(rentabilidade)
    
    def depositar(self, valor): # mudando o comportamento do método herdado da classe Contabancaria
        self.saldo += valor
        if self.saldo >= 1000:
            self.rentabilidade_total += 0.1
            print(f'Parabens, sua retabilidade aumentou para {self.rentabilidade_total:.2f}')
        self.ver_saldo()

class ContaCorrente(ContaBancaria):
    def depositar(self, valor):
        if valor < 100:
            raise Exception('O valor minimo é 100')
        else:
            super(ContaCorrente, self).depositar(valor)

conta_corrente = ContaCorrente()
conta_corrente.depositar(100)