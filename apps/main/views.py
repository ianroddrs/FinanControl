from django.shortcuts import render
from .models import Emprestimos, Pagamentos

def home(request):
   return render(request, 'index.html')

def emprestimos(request):
    code_id = request.GET.get('code_id')
    emprestimo = Emprestimos.objects.get(code_id=code_id)
    pagamentos = Pagamentos.objects.filter(emprestimo_id=emprestimo['id'])

    context = {
        'emprestimo': emprestimo,
        'pagamentos': pagamentos
    }
    return render(request, 'emprestimos.html', context)

def dashboards(request):
    emprestimos = Emprestimos.objects.all()
    pagamentos = Pagamentos.objects.all()

    total_emprestado = sum([emprestimo['valor_emprestado'] for emprestimo in emprestimos])
    saldo_total = sum([emprestimo['saldo_atual'] for emprestimo in emprestimos])
    total_pago = sum([emprestimo['total_pago'] for emprestimo in emprestimos])
    lucro = saldo_total - (total_emprestado - total_pago)

    context = {
        'emprestimos': emprestimos,
        'pagamentos': pagamentos,
        'total_emprestado': total_emprestado,
        'saldo_total': saldo_total,
        'total_pago': total_pago,
        'lucro': lucro
    }

    return render(request, 'dashboards.html', context)


















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
          total pago: ${total_pago}
      """
      print(texto)
