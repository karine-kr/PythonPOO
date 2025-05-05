class CaixaDoAtacado:
    def __init__(self, cardapio):
        self.cardapio = cardapio

    def computarCompra(self, compras:str) -> float:
        try:
            with open(compras, "r") as file:
                linhas = [linha.strip() for linha in file if linha.strip()]
        except FileNotFoundError: 
                print("O arquivo não encontrado!")
                return 0.0

        metodo_pagamento = linhas[0].lower()
        itens_compra = linhas[1:]

        print(f"\nMétodo de pagamento selecionado: {metodo_pagamento}\n")
        
        subtotal_geral = 0.0
        total = 0

        for linha in itens_compra:
            partes = linha.split(",")
            if len(partes) !=2:
                print(f"Linha mal formatada: {linha}")
                continue

            id_str, qtd_str = partes
            try:
                id_produto  = int(id_str.strip())
                quantidade = int (qtd_str.strip())
            except ValueError:
                 print(f"Valores inválidos na linha: {linha}")
                 continue
            
            produto = self.cardapio.get(id_produto)
            if not produto:
                print(f"Produto com ID {id_produto} não encontrado no cardápio!!")
                continue

            preco_unitario = produto.preco
            subtotal = preco_unitario * quantidade

            percentual_desconto = self._desconto_quantidade(quantidade)
            subtotal_com_desconto = subtotal * (1 - percentual_desconto)
            subtotal_geral += subtotal_com_desconto
            total += quantidade
                
            print(f"Produto: {produto.nome}")
            print(f" Quantidade: {quantidade}")
            print(f" Preço unitário: R${preco_unitario:.2f}")
            print(f" Subtotal: R${subtotal:.2f}")
            print(f" Desconto aplicado: {int(percentual_desconto*100)}%")
            print(f" Subtotal somente com o desconto referente a quantidade de produto: R${subtotal_com_desconto:.2f}\n")

        total_final = self._ajuste_pagamento(subtotal_geral, metodo_pagamento)

        print(f"\nQuantidade total de itens: {total}")
        print(f"Total com desconto somente da quantidade de produto: R${subtotal_geral:.2f}")
        print(f"Total Final com os ajustes de pagamentos: R${total_final:.2f}")

        return round(total_final, 2)
              
    def _desconto_quantidade(self, quantidade: int) -> float:
        quantidade = int(quantidade)
        if 11 <= quantidade <=20:
            return 0.10
        elif 21 <= quantidade <=50:
            return 0.20
        elif quantidade > 50:
            return 0.25
        return 0.0
    
    def _ajuste_pagamento(self, total, metodo_pagamento):
        if metodo_pagamento == "dinheiro":
            return total * 0.95
        elif metodo_pagamento == "credito":
            return total * 1.03
        return total