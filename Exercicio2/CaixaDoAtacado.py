class CaixaDoAtacado:

    CARDAPIO = {
      1: {"nome": "Café 1kg", "preco": 53},
      2: {"nome": "Sabão em pó", "preco": 36},
      3: {"nome": "Caixa de Leite", "preco": 82},
      4: {"nome": "Refrigerate", "preco": 8.50}
    }

    @staticmethod
    def desconto_quantidade(quantidade):
        if 11 <= quantidade <=20:
            return 0.10
        elif 21 <= quantidade <=50:
            return 0.20
        elif quantidade > 50:
            return 0.25
        return 0.0
    
    @staticmethod
    def ajuste_pagamento(metodo):
        ajustes = {
            "debito": 1.00,
            "dinheiro": 0.95,
            "credito": 1.03
        }
        return ajustes.get(metodo.lower(), 1.00)
    
    def computarCompra(self, compras):
        try:
            with open(compras, "r") as file:
                linhas = [linha.strip().replace(",", " ") for linha in file.readlines() if linha.strip()]

            if not linhas: 
                print("O arquivo está vazio!")
                return None

            metodo_pagamento = linhas[0].lower()
            print(f"\nMétodo de pagamento selecionado: {metodo_pagamento}\n")

            if metodo_pagamento not in ["debito", "dinheiro", "credito"]:
                print("Método de pagamento inválido!")
                return None
            
            itens_compra = [linha.split() for linha in linhas[1:]]

            total = 0

            for item in itens_compra:
                if len(item) != 2:
                    print(f"Formato inválido na linha: {item}")
                    continue

                try:
                    id_produto, quantidade = int(item[0]), int(item[1])
                except ValueError:
                    print(f"Erro ao converter valores na linha: {item}")
                    continue

                if id_produto in self.CARDAPIO:
                    produto = self.CARDAPIO[id_produto]                
                    preco_unitario  = produto["preco"]
                    subtotal = preco_unitario * quantidade
                    desconto_qtd = self.desconto_quantidade(quantidade)
                    subtotal *= (1 - desconto_qtd)

                    print(f"Produto selecionado: {produto['nome']}, Quantidade: {quantidade}, Subtotal com desconto referente ao valor das unidades: {subtotal:.2f}")

                    total += subtotal

                else:
                    print(f"Produto com ID {id_produto} não encontrado no cardápio!!")
            
            ajuste_pag = self.ajuste_pagamento(metodo_pagamento)
            total *= ajuste_pag

            print(f"\nTotal com ajustado levando em consideração as regras de pagamento ser débito, dinheiro ou crédito: {total:.2f}\n")

            return round(total, 2)

        except Exception as e:
            print(f"Erro ao processar o arquivo: {e}")
            return None