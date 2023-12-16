class ContaBancaria(object):
    def __init__(self, titular, saldo):
        self.titular = ''
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de {valor:.2f} realizado com sucesso.')
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insufuciente')
        else:
            self.saldo -= valor
            print(f'Saque de {valor:.2f} realizado com sucesso.')
    def obter_saldo(self):
        print(f"Saldo Atual: {self.saldo:.2f}")

nome = input('Nome do titular: ')
conta_bancaria = ContaBancaria(saldo=0, titular=nome)
print(f'Olá {nome} seja Bem-vindo ao Nubanco\n')

def menu():
    print('1) Ver Saldo')
    print('2) Deposito')
    print('3) Sacar')
    print('0) Sair')
    op = int(input('>> '))
    while op not in [0, 1, 2, 3]:
        print('opção inválida')
        op = int(input('\n>> '))
    
    return op

while True:
    op = menu()

    match op:
        case 1:
            conta_bancaria.obter_saldo()
        case 2:
            valor = float(input('Digite o valor: '))
            conta_bancaria.depositar(valor)
        case 3:
            try: 
                valor = float(input('Digite o valor: '))
                conta_bancaria.sacar(valor)
            except:
                print('Tente novamente...')
        case 0:
            break


