"""
EXERCÍCIO 10.1 - GerenciadorDeVendas

CODE SMELLS IDENTIFICADOS:
1. Long Method: um único método calcula total, aplica desconto, cobra,
   gera relatório e grava em arquivo.
2. Violação do SRP / Divergent Change: a classe muda por 4 motivos
   (regra de cálculo, desconto, pagamento, relatório).
3. Comentários como "separadores" (# Lógica de cálculo, # Lógica de desconto...):
   cada bloco comentado é, na verdade, uma função esperando para ser extraída.
4. Magic Numbers / Magic Strings: 0.90, 'VIP', 'CARTAO', 'BOLETO'.
5. Cadeia if/elif de pagamento (viola Open/Closed): novo meio de pagamento
   obriga a editar o método.

REFATORAÇÕES APLICADAS:
- Extract Method (calcular_total, aplicar_desconto)
- Extract Class (Pagamento, GeradorDeRelatorio)
- Replace Conditional with Polymorphism (Strategy) para os pagamentos
- Replace Magic Number with Constant
"""
from abc import ABC, abstractmethod

DESCONTO_VIP = 0.10
TIPO_CLIENTE_VIP = "VIP"


# ---------- Pagamento (Strategy) ----------
class Pagamento(ABC):
    @abstractmethod
    def cobrar(self, total):
        ...


class PagamentoCartao(Pagamento):
    def cobrar(self, total):
        print(f"Cobrando R$ {total} no cartão de crédito...")


class PagamentoBoleto(Pagamento):
    def cobrar(self, total):
        print(f"Gerando boleto no valor de R$ {total}...")


# ---------- Relatório ----------
class GeradorDeRelatorio:
    def __init__(self, arquivo="relatorio_vendas.txt"):
        self.arquivo = arquivo

    def gerar(self, cliente, total):
        return f"--- Relatório de Venda ---\nCliente: {cliente['nome']}\nTotal: R$ {total}\n"

    def salvar(self, cliente, total):
        with open(self.arquivo, "a") as f:
            f.write(self.gerar(cliente, total))


# ---------- Classe principal (apenas orquestra) ----------
class GerenciadorDeVendas:
    METODOS_PAGAMENTO = {
        "CARTAO": PagamentoCartao(),
        "BOLETO": PagamentoBoleto(),
    }

    def __init__(self, gerador_relatorio=None):
        self.gerador_relatorio = gerador_relatorio or GeradorDeRelatorio()

    def processar_venda(self, itens, cliente, metodo_pagamento):
        total = self.calcular_total(itens)
        total = self.aplicar_desconto(total, cliente)
        self.cobrar(total, metodo_pagamento)
        self.gerador_relatorio.salvar(cliente, total)
        print("Venda processada com sucesso.")

    @staticmethod
    def calcular_total(itens):
        return sum(item["preco"] * item["quantidade"] for item in itens)

    @staticmethod
    def aplicar_desconto(total, cliente):
        if cliente["tipo"] == TIPO_CLIENTE_VIP:
            return total * (1 - DESCONTO_VIP)
        return total

    def cobrar(self, total, metodo_pagamento):
        pagamento = self.METODOS_PAGAMENTO.get(metodo_pagamento)
        if pagamento is None:
            raise ValueError(f"Método de pagamento desconhecido: {metodo_pagamento}")
        pagamento.cobrar(total)


if __name__ == "__main__":
    itens = [{"preco": 50.0, "quantidade": 2}, {"preco": 20.0, "quantidade": 1}]
    cliente = {"nome": "Maria", "tipo": "VIP"}
    GerenciadorDeVendas().processar_venda(itens, cliente, "CARTAO")
