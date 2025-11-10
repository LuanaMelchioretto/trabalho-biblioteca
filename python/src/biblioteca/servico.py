def calcular_multa(dias_emprestimo: int) -> float:
    if dias_emprestimo < 0:
        raise ValueError("Dias empréstimo não pode ser negativo")
    return max(0, dias_emprestimo - 7) * 2.0
