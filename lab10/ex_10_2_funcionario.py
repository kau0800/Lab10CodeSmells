"""
EXERCÍCIO 10.2 - Funcionario

CODE SMELLS IDENTIFICADOS:
1. Long Parameter List: construtor com 11 parâmetros.
2. Data Clumps: rua, numero, bairro, cidade, estado, cep sempre aparecem
   juntos (endereço); ddd + telefone_numero também (telefone).
3. Large Class / Baixa coesão: Funcionario guarda dados de endereço e telefone
   que não são responsabilidade dele.
4. Primitive Obsession: endereço e telefone representados por primitivos soltos.

REFATORAÇÕES APLICADAS:
- Extract Class (Endereco e Telefone)
- Introduce Parameter Object (Funcionario recebe objetos, não 11 valores)
- Move Method (formatação do endereço/telefone vai para as próprias classes)
"""


class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return (f"{self.rua}, {self.numero} - {self.bairro}, "
                f"{self.cidade}/{self.estado} - CEP: {self.cep}")


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f"({self.ddd}) {self.numero}"


class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Funcionario: {self.nome} - {self.cargo}")
        print(f"Contato: {self.telefone}")
        print(f"Endereço: {self.endereco}")


if __name__ == "__main__":
    f = Funcionario(
        "Ana", "Analista", 5000,
        Endereco("Rua A", 10, "Centro", "São Paulo", "SP", "01000-000"),
        Telefone("11", "99999-0000"),
    )
    f.exibir_dados()
