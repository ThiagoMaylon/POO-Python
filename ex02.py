class Livro(object):
    def __init__(self, nome, autor, ano):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.situacao = "Disponível"
    
    def emprestar(self):
        self.situacao = "Emprestado"
    def devolver(self):
        self.situacao = "Disponível"

class Biblioteca(Livro):
    def __init__(self):
        self.livros = []
    
    def listar_livros(self):
        print('Livros na Biblioteca:')
        for index, livro in enumerate(self.livros):
            print(f'{index + 1}. {livro.nome}, {livro.autor}, {livro.ano} ({livro.situacao})')
    
    def adicionar_livros(self, livro):
        self.livros.append(livro)

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)

biblioteca = Biblioteca()
print('\n')
# adcionando os livros
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)
biblioteca.listar_livros()
print('\n')
# emprestando livro
livro2.emprestar()
biblioteca.listar_livros()
print('\n')
livro2.devolver()
biblioteca.listar_livros()


