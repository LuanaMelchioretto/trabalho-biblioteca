from datetime import date
from .modelos import Emprestimo

def calcular_multa(data_emprestimo: date, data_devolucao: date, dias_prazo: int = 7, multa_por_dia: float = 2.0) -> float:
    dias_atraso = (data_devolucao - data_emprestimo).days - dias_prazo
    if dias_atraso > 0:
        return dias_atraso * multa_por_dia
    return 0.0

class BibliotecaService:
    def __init__(self, repo, email_service=None, relogio=None):
        self.repo = repo
        self.email = email_service
        self.relogio = relogio

    def emprestar(self, usuario_id, livro_id):
        usuario = self.repo.usuarios[usuario_id]
        livro = self.repo.livros[livro_id]
        ativos = [
            e
            for e in self.repo.emprestimos
            if e.usuario_id == usuario_id and e.data_devolucao is None
        ]
        if len(ativos) >= usuario.limite:
            raise ValueError("Limite de empréstimos atingido")
        if not livro.disponivel:
            raise ValueError("Livro não disponível")
        livro.disponivel = False
        emp = Emprestimo(
            usuario_id=usuario_id,
            livro_id=livro_id,
            data_emprestimo=(self.relogio.hoje() if self.relogio else date.today()),
        )
        self.repo.salvar_emprestimo(emp)
        return emp
