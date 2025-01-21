from core.services import Model
from datetime import datetime

class Negociacoes(metaclass=Model):
    id = int
    code_id = str
    nome_pessoa = str
    valor_emprestado = float
    saldo_atual = float
    juros_mensal = float
    total_pago = float

    class Meta:
        db_name = "financontrol_db"
        db_table = "negociacoes"

class Pagamentos(metaclass=Model):
    id = int
    emprestimo_id = int
    valor_pagamento = float
    valor_juros = float
    data_pagamento = datetime

    class Meta:
        db_name = "financontrol_db"
        db_table = "pagamentos"