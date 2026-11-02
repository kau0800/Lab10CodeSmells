"""
EXERCÍCIO 10.7 - verificar_frete_internacional

CODE SMELLS IDENTIFICADOS:
1. Message Chains (cadeia de mensagens):
   pedido.cliente.endereco.estado.pais.nome
   O cliente conhece toda a estrutura interna de 5 objetos.
2. Viola a Lei de Demeter ("fale só com seus amigos próximos").
3. Acoplamento alto: se a estrutura mudar (ex.: Endereco passar a ter 'cidade'
   entre estado e país), TODO código que usa a cadeia quebra.

REFATORAÇÕES APLICADAS:
- Hide Delegate: cada classe expõe um método que esconde o próximo elo
  (Pedido.pais_destino -> Cliente.pais -> Endereco.pais -> Estado.pais.nome)
- O código cliente agora faz apenas: pedido.pais_destino()
"""


class Pais:
    def __init__(self, nome):
        self.nome = nome


class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self._pais = pais

    def nome_do_pais(self):
        return self._pais.nome


class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self._estado = estado

    def nome_do_pais(self):
        return self._estado.nome_do_pais()


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self._endereco = endereco

    def nome_do_pais(self):
        return self._endereco.nome_do_pais()


class Pedido:
    def __init__(self, cliente, valor):
        self._cliente = cliente
        self.valor = valor

    def pais_destino(self):
        return self._cliente.nome_do_pais()


PAIS_ORIGEM = "Brasil"


def verificar_frete_internacional(pedido):
    if pedido.pais_destino() != PAIS_ORIGEM:
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão.")


if __name__ == "__main__":
    br = Pais("Brasil")
    pt = Pais("Portugal")
    p1 = Pedido(Cliente("Ana", Endereco("Rua A", Estado("SP", br))), 100)
    p2 = Pedido(Cliente("Rui", Endereco("Rua B", Estado("Lisboa", pt))), 100)
    verificar_frete_internacional(p1)
    verificar_frete_internacional(p2)
