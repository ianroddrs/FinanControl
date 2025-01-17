from django.shortcuts import render
from .models import Emprestimos, Pagamentos
import qrcode
import io
import base64

def home(request):
   return render(request, 'index.html')

def emprestimos(request):
    code_id = request.GET.get('code_id')
    emprestimo = Emprestimos.objects.get(code_id=code_id)
    pagamentos = Pagamentos.objects.filter(emprestimo_id=emprestimo['id'])

    valor_juros = emprestimo['saldo_atual'] * (emprestimo['juros_mensal']/100)

    pix = pix_code(0)

    context = {
        'emprestimo': emprestimo,
        'pagamentos': pagamentos,
        'valor_juros': valor_juros,
        'pix':pix
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

# Função principal para gerar o QR Code
def pix_code(value):
    pix_value = float(value) if value else 0
    pix_key = '+5591989055041'  # Altere para qualquer chave PIX: Celular, CPF, CNPJ ou chave aleatória.
    destinatario = 'Ian Mateus Alves Rodrigues'  # Digite aqui o destinatário
    cidade = 'SAO PAULO'  # Digite aqui a cidade com máximo de 24 caracteres

    # Construindo o Payload PIX a partir dos dados adicionados.
    payload = build_pix_payload(pix_key, pix_value, destinatario, cidade)

    # Calcula o CRC16 e o adiciona ao payload PIX
    crc16 = get_crc16(payload)
    payload += '6304' + format(crc16, 'X').upper()

    qr = qrcode.make(payload)
    img_buffer = io.BytesIO()
    qr.save(img_buffer, format="PNG")
    img_buffer.seek(0)
    qr_code = base64.b64encode(img_buffer.read()).decode('utf-8')

    return {'qr_code': qr_code, 'code': payload}


# Função para construir o Payload PIX
def build_pix_payload(pix_key, pix_value, destinatario, cidade):
    pix_value_formatted = f"{pix_value:.2f}"
    pix_length_value = len(pix_value_formatted)
    pix_length_formatted = str(pix_length_value).zfill(2)
    destinatario_length = len(destinatario)
    cidade_length = str(len(cidade)).zfill(2)

    return (
        f'00020126360014BR.GOV.BCB.PIX01{len(pix_key)}{pix_key}'
        f'52040000530398654{pix_length_formatted}{pix_value_formatted}'
        f'5802BR59{destinatario_length}{destinatario}'
        f'60{cidade_length}{cidade}62130509financontrol'
    )


# Função para calcular o CRC16
def get_crc16(payload):
    payload += '6304'
    polinomio = 0x1021
    resultado = 0xFFFF
    length = len(payload)

    for offset in range(length):
        resultado ^= (ord(payload[offset]) << 8)

        for _ in range(8):
            if (resultado << 1) & 0x10000:
                resultado ^= polinomio
            resultado &= 0xFFFF

    return resultado













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
