from biblioteca import Biblioteca, LivroJaExisteException, LivroIndisponivelException, LivroNaoEmprestadoException

def exibir_menu():
    print("\n ############## Gerenciador de biblioteca da Karine: #############")
    print("1 - Adicionar Livro")
    print("2 - Emprestar Livro")
    print("3 - Devolver Livro")
    print("4 - Listar Livros")
    print("5 - Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção de 1 a 5: ")

        if opcao == "1":
            titulo = input("\nDigite o título do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            try:
                biblioteca.adicionar_livro(titulo,autor)
            except LivroJaExisteException as e:
                print(e)

        elif opcao == "2":
            titulo = input("\nDigite o titulo do livro  para emprestrar: ")
            try:
                biblioteca.emprestar_livro(titulo)
            except LivroIndisponivelException as e:
                print(e)

        elif opcao == "3":
            titulo = input("\nDigite o título do livro para devolver: ")
            try:
                biblioteca.devolver_livro(titulo)
            except LivroNaoEmprestadoException as e:
                print(e)
        
        elif opcao == "4":
            biblioteca.listar_livros()

        elif opcao == "5":
            print("\nEncerrando o programa! Obrigada por pela visita na bliblioteca da Karine.\n")
            break

        else:
            print("\nOpçção inválida!! Tente novamente: ")

if __name__ == "__main__":
    main()