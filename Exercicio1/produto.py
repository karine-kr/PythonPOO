import json

class Produto:

    def __init__(self, id,  nome, quantidade,preco):
        self.id = int(id)
        self.nome = nome
        self.quantidade = int(quantidade)
        self.preco = float(preco)

    def __str__(self):
        return f"IDENTIFICADOR: {self.id}, PRODUTO: {self.nome}, PREÇO: R$ {self.preco:.2f}, QUANTIDADE: {self.quantidade}"
