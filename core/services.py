import os
import gspread
from typing import List, Dict, Any
from django.conf import settings

def initialize_gspread() -> gspread.client.Client:
  """
  Initialize a gspread client with the given credentials.
  """
  return gspread.service_account_from_dict(get_credentials())  # Note: we could move this to settings to do this once.

def get_credentials() -> dict:
  """
  Return gspread credentials.
  """
  return {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN")
  }

class GSpreadModel():
  def __init__(self, sheet_name: str, worksheet_name: str = None):
    """
    Inicializa a classe Emprestimos com acesso à planilha e worksheet.
    """
    self.client = settings.GSPREAD_CLIENT
    self.sheet = self.client.open(sheet_name)
    self.worksheet = self.sheet.get_worksheet(0) if worksheet_name is None else self.sheet.worksheet(worksheet_name)

  def using(self, name: str):
    """
    Muda a aba atual (worksheet).
    """
    self.worksheet = self.sheet.worksheet(name)

  def get_line(self, num: int) -> List[str]:
    """
    Retorna os valores de uma linha específica.
    """
    return self.worksheet.row_values(num)

  def get_col(self, num: int) -> List[str]:
    """
    Retorna os valores de uma coluna específica.
    """
    return self.worksheet.col_values(num)

  def get_cell(self, line: int, col: int) -> str:
    """
    Retorna o valor de uma célula específica.
    """
    return self.worksheet.cell(line, col).value

  def get_all_values(self) -> List[Dict[str, Any]]:
    """
    Retorna todas as linhas como uma lista de dicionários.
    """
    return self.worksheet.get_all_records()

  def add_row(self, data: List[Any]):
    """
    Adiciona uma nova linha com os valores fornecidos.
    """
    self.worksheet.append_row(data)

  def update_cell(self, line: int, col: int, value: Any):
    """
    Atualiza o valor de uma célula específica.
    """
    self.worksheet.update_cell(line, col, value)

  def update_row(self, row_num: int, data: List[Any]):
    """
    Atualiza uma linha inteira com os valores fornecidos.
    """
    for col_num, value in enumerate(data, start=1):
        self.worksheet.update_cell(row_num, col_num, value)

  def delete_row(self, row_num: int):
    """
    Exclui uma linha específica da planilha.
    """
    self.worksheet.delete_row(row_num)

  def search(self, query: str, column: int) -> List[Dict[str, Any]]:
    """
    Busca registros em uma coluna específica que correspondam ao valor.
    """
    records = self.get_all_values()
    results = [record for record in records if record[list(record.keys())[column - 1]] == query]
    return results
