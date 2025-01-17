from core.services import Model
from datetime import datetime

class Emprestimos(metaclass=Model):
    id = int
    code_id = str
    nome_pessoa = str
    valor_emprestado = float
    saldo_atual = float
    juros_mensal = float
    total_pago = float

    class _meta:
        db_name = "emprestimos_db"
        db_table = "emprestimos"

class Pagamentos(metaclass=Model):
    id = int
    emprestimo_id = int
    valor_pagamento = float
    valor_juros = float
    data_pagamento = datetime

    class _meta:
        db_name = "emprestimos_db"
        db_table = "pagamentos"