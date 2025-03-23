from contato import Contato 
from agendaTelefonica import AgendaTelefonica

def menuUsuario():
    agenda = AgendaTelefonica()


    while True:
        print("\n =========== MENU DA AGENDA TELEFONICA DA KARINE ===========")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar contato")
        print("4. Atualizar Contato")
        print("5. Listar Contatos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            if agenda.adicionar_contato(Contato(nome, telefone)):
                print("\nContato adicionado com sucesso!!")
        
        elif opcao == "2":
            nome = input("Nome do contato a remover: ")
            if agenda.remover_contato(nome):
                print("\nContato removido com sucesso!!")
            else:
                print("\nContato não encontrado!")

        elif opcao == "3":
            nome = input ("Nome do contato que deseja buscar na agênda: ")
            contato = agenda.buscar_contato(nome)
            if contato:
                print(f"\nContato encontrado: {contato}")
            else: 
                print(f"\nContato não encontrado!!")

        elif opcao == "4":
            nome_antigo = input ("Nome do contato que deseja atualizar: ")
            contato = agenda.buscar_contato(nome_antigo)

            if contato:
                novo_nome = input(f"Informe novo nome (ou pressione 'Enter' para manter {contato.nome}): ").strip()
                novo_telefone = input (f"Informe novo telefone (ou pressione 'Enter' para manter {contato.telefone}): ").strip()

                if not novo_nome:
                    novo_nome = contato.nome
                if not novo_telefone:
                    novo_telefone = contato.telefone

                if agenda.atualizar_contato(nome_antigo, novo_nome,  novo_telefone):
                    print("\nContato atualizado com sucesso!")
                else:
                    print("\nFalha ao atualizar o contato!!")
                
            else:
                print("\nContato não encontrado!!")

        elif opcao == "5":
            agenda.listar_contatos()

        elif opcao == "6":
            print ("\nFechando o programa.")
            break
        else: 
            print ("\nOpção inválida!! Tente novamente uma opção: ")

if __name__ == "__main__":
    menuUsuario()
    




        

