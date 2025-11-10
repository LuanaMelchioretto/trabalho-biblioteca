import pytest
from src.biblioteca.servico import BibliotecaService
from src.biblioteca.relogio import RelogioStub
from src.biblioteca.repositorio import InMemoryRepo
from src.biblioteca.modelos import Livro, Usuario

def test_emprestar_livro_e_altera_disponibilidade():
    repo = InMemoryRepo()
    repo.salvar_usuario(Usuario("u1","Ana", limite=1))
    repo.salvar_livro(Livro("l1","T", True))
    service = BibliotecaService(repo, relogio=RelogioStub())
    service.emprestar("u1","l1")
    assert repo.livros["l1"].disponivel is False
