from livro import Livro

class LivroJaExisteException(Exception):
    pass

class LivroIndisponivelException(Exception):
    pass

class LivroNaoEmprestadoException(Exception):
    pass

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def adicionar_livro(self, titulo, autor):
        if titulo in self.livros:
            raise LivroJaExisteException(f'\nErro! O Livro "{titulo}" já existe na biblioteca.')
        self.livros[titulo] = Livro(titulo, autor)
        print(f'\nLivro "{titulo}" adicionado com sucesso!! ')

    def emprestar_livro(self, titulo):
        livro = self.livros.get(titulo)
        if not livro or not livro.disponivel:
            raise LivroIndisponivelException(f'\nErro! O livro "{titulo}" não está disponível para emprestimo no momento.')
        livro.emprestar()
        print(f'\nLivro "{titulo}" emprestado com sucesso!!')

    def devolver_livro(self, titulo):
        livro = self.livros.get(titulo)
        if not livro or livro.disponivel:
            raise LivroNaoEmprestadoException(f'\nErro! O livro "{titulo}" não está emprestado, então não pode ser devolvido!')
        livro.devolver()
        print(f'\nLivro "{titulo}" devolvido com sucesso"!!')

    def listar_livros(self):
        if not self.livros:
            print("\nA biblioteca está vazia!!")
        else:
            print("\n Livros disponíveis na biblioteca: ")
            for titulo, livro in self.livros.items():
                status = "Disponivel" if livro.disponivel else "Emprestado"
                print(f' - {titulo} ({livro.autor}) -> {status}')
