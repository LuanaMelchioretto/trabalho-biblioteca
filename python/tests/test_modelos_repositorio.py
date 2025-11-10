from src.biblioteca.modelos import Livro, Usuario, Emprestimo
from src.biblioteca.repositorio import InMemoryRepo

def test_repositorio_salva_e_recupera():
    repo = InMemoryRepo()
    u = Usuario("u1", "Ana")
    l = Livro("l1", "Titulo", True)
    repo.salvar_usuario(u)
    repo.salvar_livro(l)
    assert repo.usuarios["u1"].nome == "Ana"
    assert repo.livros["l1"].titulo == "Titulo"
