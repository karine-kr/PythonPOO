from contato import Contato 
from agendaTelefonica import AgendaTelefonica

class MenuUsuario():
    def __init__(self):
        self.agenda = AgendaTelefonica()

    def iniciar(self) -> None:
            while True:
                print("\n =========== MENU DA AGENDA TELEFONICA DA KARINE ===========")
                print("1. Adicionar Contato")
                print("2. Remover Contato")
                print("3. Buscar contato")
                print("4. Atualizar Contato")
                print("5. Listar Contatos")
                print("6. Sair")

                opcao = input("Escolha uma opção: ").strip()
                if opcao == "1":
                    self.adicionar()
                elif opcao == "2":
                    self.remover()
                elif opcao == "3":
                    self.buscar()
                elif opcao == "4":
                    self.atualizar()
                elif opcao == "5":
                    self.agenda.listar_contatos()
                elif opcao == "6":
                    print("\nFechando o programa.")
                    break
                else:
                    print("\nOpção inválida! Tente novamente.")
        
    def adicionar(self) -> None:
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        if self.agenda.adicionar_contato(Contato(nome, telefone)):
            print("\nContato adicionado com sucesso!")
        
    def remover(self) -> None:
        nome = input("Nome do contato a remover: ").strip()
        if self.agenda.remover_contato(nome):
            print("\nContato removido com sucesso!")
        else:
            print("\nContato não encontrado!")
    
    def buscar(self) -> None:
        nome = input("Nome do contato a buscar: ").strip()
        contato = self.agenda.buscar_contato(nome)
        if contato:
            print(f"\nContato encontrado: {contato}")
        else:
            print("\nContato não encontrado!")
    
    def atualizar(self) -> None:
        nome_antigo = input("Nome do contato a atualizar: ").strip()
        contato = self.agenda.buscar_contato(nome_antigo)
        if contato:
            novo_nome = input(f"Novo nome (pressione Enter para manter '{contato.nome}'): ").strip()
            novo_telefone = input(f"Novo telefone (pressione Enter para manter '{contato.telefone}'): ").strip()
            novo_nome = novo_nome if novo_nome else contato.nome
            novo_telefone = novo_telefone if novo_telefone else contato.telefone
            novo_contato = Contato(novo_nome, novo_telefone)
            if self.agenda.atualizar_contato(nome_antigo, novo_contato):
                print("\nContato atualizado com sucesso!")
            else:
                print("\nFalha ao atualizar o contato.")
        else:
            print("\nContato não encontrado.")
