from contato import Contato 

class AgendaTelefonica:
    
    def __init__(self):
        self.contatos = []

    def adicionar_contato (self,contato):
        if self.buscar_contato(contato.nome):
            print("\nContato com este nome já existe!")
            return False
        self.contatos.append(contato)
        return True
    
    def remover_contato (self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
            return True
        return False
    
    def buscar_contato (self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None
    
    def atualizar_contato(self, nome_antigo, novo_nome, novo_telefone):
        contato = self.buscar_contato(nome_antigo)
        if contato:
            if novo_nome.lower() != nome_antigo.lower() and self.buscar_contato(novo_nome):
                print("\nJá exsite um contato com esse novo nome!!")
                return False
            
            contato.nome = novo_nome
            contato.telefone = novo_telefone
            return True
        return False
    
    def listar_contatos(self):
        if not self.contatos:
            print("\nA agenda está vazia!!!")
        else:
            print("\nLista de contatos: ")
            for contato in self.contatos:
                print(contato)


