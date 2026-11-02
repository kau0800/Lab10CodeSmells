"""
EXERCÍCIO 10.6 - ProcessadorFinanceiro

CODE SMELLS IDENTIFICADOS:
1. Duplicated Code: crédito e débito têm a mesma estrutura, diferindo só na
   taxa (5% x 2%) e no nome.
2. Comments (smell): comentários que apenas repetem o que o código já diz
   ("Imprime o valor na tela", "Verifica se o valor é maior que zero").
   Código bom se explica por nomes, não por comentários redundantes.
3. Magic Numbers: 0.05 e 0.02 sem nome.
4. Lógica de negócio misturada com saída (print) e validação.

REFATORAÇÕES APLICADAS:
- Extract Method / Parameterize Method (_processar com taxa e nome)
- Replace Magic Number with Constant (TAXA_CREDITO, TAXA_DEBITO)
- Remoção de comentários redundantes; métodos com nomes expressivos
  (_valor_e_valido, _aplicar_taxa)
"""

TAXA_CREDITO = 0.05
TAXA_DEBITO = 0.02


class ProcessadorFinanceiro:
    def processar_pagamento_credito(self, valor):
        self._processar("crédito", valor, TAXA_CREDITO)

    def processar_pagamento_debito(self, valor):
        self._processar("débito", valor, TAXA_DEBITO)

    def _processar(self, tipo, valor, taxa):
        if not self._valor_e_valido(valor):
            print("Valor inválido")
            return
        print(f"Processando {tipo}: R$ {self._aplicar_taxa(valor, taxa)}")

    @staticmethod
    def _valor_e_valido(valor):
        return valor > 0

    @staticmethod
    def _aplicar_taxa(valor, taxa):
        return valor + valor * taxa


if __name__ == "__main__":
    p = ProcessadorFinanceiro()
    p.processar_pagamento_credito(100)
    p.processar_pagamento_debito(100)
    p.processar_pagamento_debito(-5)
