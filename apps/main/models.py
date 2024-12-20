from core.services import GSpreadModel

class Emprestimos(GSpreadModel):


    def adicionar_emprestimo(self, nome, livro, data):
        self.emprestimos.add_row([nome, livro, data])

    def buscar_emprestimos(self):
        return self.emprestimos.get_all_values()
    
    class Meta:
        db_table = 'emprestimos'
    
class Pagamentos(GSpreadModel):
    def __init__(self):
        self.emprestimos = GSpreadModel(sheet_name="emprestimos")

    def adicionar_emprestimo(self, nome, livro, data):
        self.emprestimos.add_row([nome, livro, data])

    def buscar_emprestimos(self):
        return self.emprestimos.get_all_values()