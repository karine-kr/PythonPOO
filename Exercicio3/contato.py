class Contato:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Telefone: {self.telefone}"