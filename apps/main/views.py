from django.shortcuts import render
from .models import Emprestimos

def photo_wall(request):
  # emprestimos = Emprestimos.objects.all()
  emprestimos = Emprestimos.objects.filter(juros_mensal=0.02, saldo_atual = 1200)
  print(emprestimos)
  emprestimo = Emprestimos.objects.get(id=2)
  print(emprestimo)
  return render(request, 'photowall.html', {'photos': []})


















def emp():
  # Dados iniciais
  principal = 20000  # valor do empréstimo inicial
  juros_mensal = 0.0165 # taxa de juros (2% ao mês)
  pagamentos = [700]  # pagamento nos meses subsequentes

  # Simulação dos pagamentos
  saldo = principal  # saldo inicial é igual ao valor emprestado
  total_pago = 0
  meses = 0

  # Agora, simular os pagamentos de 700 reais até quitar o saldo
  for pagamento in pagamentos:
      valor_juros = saldo * juros_mensal
      if pagamento > saldo + valor_juros:
          pagamento = saldo + valor_juros
      saldo = saldo * (1 + juros_mensal) - pagamento
      total_pago += pagamento
      meses += 1

      texto = f"""
          mes: {meses}
          valor_emprestado: ${principal:.2f}
          pagamento: ${pagamento:.2f}
          juros (1,65%): ${valor_juros:.2f}
          saldo restante: ${saldo:.2f}
          total pago: ${total_pago:.2f}
      """
      print(texto)
