"""
EXERCÍCIO 10.3 - criar_reserva

CODE SMELLS IDENTIFICADOS:
1. Long Parameter List: 10 parâmetros na função.
2. Data Clumps: (nome, cpf, email) = hóspede; (numero, tipo, valor_diaria) = quarto;
   (checkin, checkout) = período.
3. Magic Number: o valor 50 (taxa do café da manhã) está solto no código.
4. Mistura de responsabilidades: a mesma função imprime, calcula dias e calcula preço.
5. Primitive Obsession: tudo é tipo primitivo, sem objetos de domínio.

REFATORAÇÕES APLICADAS:
- Introduce Parameter Object / Extract Class (Hospede, Quarto, Reserva)
- Replace Magic Number with Constant (VALOR_CAFE_DA_MANHA_POR_DIA)
- Extract Method (total_dias, calcular_total, exibir_resumo)
"""
from datetime import date

VALOR_CAFE_DA_MANHA_POR_DIA = 50


class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, valor_diaria):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria


class Reserva:
    def __init__(self, hospede, quarto, data_checkin, data_checkout,
                 possui_cafe_da_manha=False):
        self.hospede = hospede
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.possui_cafe_da_manha = possui_cafe_da_manha

    def total_dias(self):
        return (self.data_checkout - self.data_checkin).days

    def calcular_total(self):
        total = self.total_dias() * self.quarto.valor_diaria
        if self.possui_cafe_da_manha:
            total += VALOR_CAFE_DA_MANHA_POR_DIA * self.total_dias()
        return total

    def exibir_resumo(self):
        print(f"Reserva criada para {self.hospede.nome} (CPF: {self.hospede.cpf})")
        print(f"Quarto {self.quarto.numero} ({self.quarto.tipo})")
        print(f"De {self.data_checkin} até {self.data_checkout}")
        print(f"Total a pagar: R$ {self.calcular_total()}")


def criar_reserva(hospede, quarto, data_checkin, data_checkout,
                  possui_cafe_da_manha=False):
    reserva = Reserva(hospede, quarto, data_checkin, data_checkout, possui_cafe_da_manha)
    reserva.exibir_resumo()
    return reserva


if __name__ == "__main__":
    criar_reserva(
        Hospede("Carlos", "123.456.789-00", "carlos@email.com"),
        Quarto(101, "Luxo", 300),
        date(2026, 11, 10), date(2026, 11, 13),
        possui_cafe_da_manha=True,
    )
