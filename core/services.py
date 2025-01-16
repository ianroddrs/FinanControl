import os
import gspread
from typing import List, Dict, Any
from django.conf import settings
from abc import ABC, ABCMeta
from datetime import datetime

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

class GSpreadModelMeta(ABCMeta):
  def __new__(cls, name, bases, attrs):
    new_class = super().__new__(cls, name, bases, attrs)
    new_class.objects = GSpreadModelBaseManager(new_class)
    return new_class
  
  
class GSpreadModelBaseManager:
  def __init__(self, model_class):
      self.model_class = model_class

  def all(self) -> List[Dict[str, Any]]:
      instance = self.model_class()
      all_records = instance.worksheet.get_all_records()
      all_records = self.__set_type_attrs(all_records)
      return all_records
  
  def get(self, **kwargs) -> Dict[str, Any]:
    all_records = self.all()
    for record in all_records:
      if all(record.get(k) == v for k, v in kwargs.items()):
        return record
    return None
  
  def filter(self, **kwargs) -> List[Dict[str, Any]]:
    all_records = self.all()
    return [record for record in all_records if all(record.get(k) == v for k, v in kwargs.items())]
  
  def __set_type_attrs(self, queryset):
    type_attrs = {attr: type for attr, type in vars(self.model_class).items() if not attr.startswith("_") and callable(getattr(self.model_class, attr))}
    for record in queryset:
      for attr, type in type_attrs.items():
        if type == datetime:
          record[attr] = datetime.strptime(record[attr], "%Y-%m-%d")
        else:
          record[attr] = type(record[attr])  
    return queryset

  
class GSpreadModel(ABC,metaclass=GSpreadModelMeta):
  dt_name = 'emprestimos'
  worksheet_name = None
  objects = None

  def __init__(self):
    self.sheet = settings.GSPREAD_CLIENT.open(self.dt_name)
    self.worksheet = self.sheet.worksheet(self.worksheet_name)
  
