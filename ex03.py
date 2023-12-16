# Exercício: Sistema de Gerenciamento de Funcionários

class Funcionario(object):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


class Empresa(Funcionario):
    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.funcionarios = []
    
    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f'Lista de Funcionários na {self.nome_empresa}:')
        for funcionario in self.funcionarios:
            print(f'Nome: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: {funcionario.salario:.2f}')


# Criando funcionários
funcionario1 = Funcionario("Thiago", "Desenvolvedor", 20000.00)
funcionario2 = Funcionario("Bob", "Analista de Dados", 6000.00)

# Criando empresa
empresa = Empresa("TechCorp")

# Contratando funcionários
empresa.contratar(funcionario1)
empresa.contratar(funcionario2)

# Listando funcionários
empresa.listar_funcionarios()