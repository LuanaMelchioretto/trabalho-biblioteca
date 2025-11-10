from datetime import date, timedelta


class Relogio:
    def hoje(self) -> date:
        return date.today()


class RelogioStub(Relogio):
    def __init__(self, data_inicial: date | None = None):
        self._hoje = data_inicial or date.today()

    def avancar_dias(self, dias: int) -> None:
        self._hoje += timedelta(days=dias)

    def hoje(self) -> date:
        return self._hoje
