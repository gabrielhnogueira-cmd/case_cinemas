from src.repository.filme_repository import FilmeRepository


class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()

    def cadastrar_filme(self, filme):

        if filme.titulo == "":
            print("Título inválido!")
            return

        self.repository.salvar(filme)

    def listar_filmes(self):
        return self.repository.listar_filmes()