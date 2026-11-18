"""Menu inicial do FolhaFácil"""

def mostrar_menu():
    print("\n" + "-" * 48)
    print("                   MENU PRINCIPAL")
    print("-" * 48)
    print("                    FolhaFácil")
    print("          Sistema de Folha de Pagamento")
    print("-" * 48)

    print("1. Cadastrar colaborador")
    print("2. Gerar Folha de Pagamento")
    print("3. Pesquisar colaborador")
    print("4. Editar colaborador")
    print("5. Ecluir colaborador")
    print("6. Relatórios")
    print("0. Sair ")
    
    print("-" * 48)


def executar_opcao(opcao): 
 if opcao == "1":
        print("\nCadastro de colaborador")
        nome = input("Digite seu nome: ")
        salario = float(input("Digite o salário: R$ "))
        print(f"Colaborador {nome} cadastrado!")


 elif opcao == "2":
  print("\nGeração de folha de pagamento: ")
  print("Geração em andamento.")

 elif opcao == "3":
  print("\nPesquisa de colaborador: ")
  print("Pesquisa em andamento.")

 elif opcao == "4":
  print("\nEdição de colaborador: ")
  print("Edição em andamento.")
    
 elif opcao == "5":
  print("\nExclusão de colaborador: ")
  print("Exclusão em andamento.")
    
 elif opcao == "6":
  print("\nRelatórios: ")
  print("Geração de relatórios em andamento.")
    


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (0 a 6): ").strip()


        if opcao not in ("0", "1", "2", "3", "4", "5", "6"):
            print("\nEssa opção nao existe. Digite um número de 0 a 6 e tente novamente,")
            input("Pressione Enter para continuar...")
            continue


        if opcao == "0":
            print("\nVocê saiu do FolhaFácil. Até mais!")
            break


        executar_opcao(opcao)


if __name__ == "__main__":
    main()
