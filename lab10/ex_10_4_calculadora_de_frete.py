"""
EXERCÍCIO 10.4 - CalculadoraDeFrete

CODE SMELLS IDENTIFICADOS:
1. Switch Statements (cadeia if/elif sobre o tipo): lógica condicional repetida
   que cresce a cada novo transporte.
2. Violação do Open/Closed Principle: adicionar "DRONE" exige MODIFICAR a
   classe existente, em vez de apenas estendê-la.
3. Magic Numbers: 2.0, 3.5, 10.0, 8.0, 50.0, 1.0 sem nome.
4. Primitive Obsession: tipo de transporte representado por string.

REFATORAÇÕES APLICADAS:
- Replace Conditional with Polymorphism (Strategy): uma classe por transporte
- Replace Magic Number with Constant/atributo nomeado
- Registro (dict) mapeando tipo -> estratégia; novo transporte = nova classe
"""
from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def calcular(self, distancia):
        ...


class _TransporteComTarifa(Transporte):
    """Frete = distancia * valor_por_km + taxa_base."""
    VALOR_POR_KM = 0.0
    TAXA_BASE = 0.0

    def calcular(self, distancia):
        return distancia * self.VALOR_POR_KM + self.TAXA_BASE


class Moto(_TransporteComTarifa):
    VALOR_POR_KM = 2.0


class Carro(_TransporteComTarifa):
    VALOR_POR_KM = 3.5
    TAXA_BASE = 10.0


class Caminhao(_TransporteComTarifa):
    VALOR_POR_KM = 8.0
    TAXA_BASE = 50.0


class Bicicleta(_TransporteComTarifa):
    VALOR_POR_KM = 1.0


class CalculadoraDeFrete:
    TRANSPORTES = {
        "MOTO": Moto(),
        "CARRO": Carro(),
        "CAMINHAO": Caminhao(),
        "BICICLETA": Bicicleta(),
    }

    def calcular_frete(self, tipo_transporte, distancia):
        transporte = self.TRANSPORTES.get(tipo_transporte)
        if transporte is None:
            raise ValueError("Tipo de transporte desconhecido")
        return transporte.calcular(distancia)


if __name__ == "__main__":
    calc = CalculadoraDeFrete()
    print(calc.calcular_frete("CARRO", 100))
    print(calc.calcular_frete("CAMINHAO", 100))
