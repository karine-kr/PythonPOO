from CaixaDoAtacado import CaixaDoAtacado
from Produto import Produto

cardapio = {
      1: Produto (1, "Café 1kg", 53.00),
      2: Produto (2, "Sabão em pó", 36.00),
      3: Produto (3, "Caixa de Leite", 82.00),
      4: Produto (4, "Refrigerate", 8.50),
    }


caixa = CaixaDoAtacado(cardapio)
total = caixa.computarCompra("compras.txt")