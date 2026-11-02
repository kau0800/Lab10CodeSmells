"""
EXERCÍCIO 10.5 - Produto

CODE SMELLS IDENTIFICADOS:
1. Violação do SRP / Divergent Change: Produto mistura regra de negócio
   (imposto), persistência (SQL) e serialização (XML). Mudar o banco, o
   formato XML ou o imposto obriga a mexer na mesma classe.
2. Magic Number: 1.15 (alíquota de imposto sem nome).
3. Acoplamento com infraestrutura: a entidade de domínio conhece SQL e XML.
4. (Bônus de segurança) SQL montado com f-string é vulnerável a SQL Injection;
   o correto é usar query parametrizada.

REFATORAÇÕES APLICADAS:
- Extract Class: ProdutoRepository (persistência) e ProdutoXmlSerializer (XML)
- Replace Magic Number with Constant (ALIQUOTA_IMPOSTO)
- Produto fica só com dados e regra de negócio
"""

ALIQUOTA_IMPOSTO = 0.15


class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * (1 + ALIQUOTA_IMPOSTO)


class ProdutoRepository:
    def salvar(self, produto):
        # Em um banco real, usar query parametrizada:
        # cursor.execute("INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?)", params)
        sql = "INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?);"
        params = (produto.id_produto, produto.nome, produto.preco)
        print(f"{sql} -> {params}")


class ProdutoXmlSerializer:
    def serializar(self, produto):
        return (f"<produto><id>{produto.id_produto}</id>"
                f"<nome>{produto.nome}</nome>"
                f"<preco>{produto.preco}</preco></produto>")


if __name__ == "__main__":
    p = Produto(1, "Teclado", 100.0)
    print(p.calcular_preco_com_imposto())
    ProdutoRepository().salvar(p)
    print(ProdutoXmlSerializer().serializar(p))
