from produto import Produto
import json

class Mercado:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def exibir_estoque(self): 
        if not self.produtos:
            print("O estoque está vazio no momento!")
            return
        print("\n#################### ESTOQUE DO MERCADO: #################### \n ")
        valor_total = 0
        for produto in self.produtos:
            print(produto)
            valor_total += produto.preco * produto.quantidade

        print(f"\nO valor total dos produtos no estoque no momento é R$ {valor_total:.2f}\n")
    

def carregar_produtos_de_arquivo(listaProdutos, mercado):
    try:
        with open(listaProdutos, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            for item in dados.get("produtos", []):
                if all(k in item for k in ["id","nome", "quantidade", "preco"]):
                    produto = Produto(item["id"], item["nome"], item["quantidade"], item["preco"])
                    mercado.adicionar_produto(produto)
                else:
                    print(f"Erro: Produto inválido no arquivo JSON -> {item}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{listaProdutos}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{listaProdutos}' não contem um JSON válido.")
mercado = Mercado()
carregar_produtos_de_arquivo("listaProdutos.json", mercado)
mercado.exibir_estoque()
