import database
import enem


# Cria as tabelas do banco de dados
database.criar_tabelas()


while True:

    print("\n========== PERSONALIZE - ENEM ==========")
    print("1 - Cadastrar Questão (Professor)")
    print("2 - Listar Questões Cadastradas")
    print("3 - Excluir Questão (Professor)")
    print("4 - Fazer Simulado (Aluno)")
    print("5 - Ver Histórico de Desempenho")
    print("6 - Sair")
    print("========================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        senha = input("Digite a senha do professor: ")

        if senha == "1234":
            enem.cadastrar()
        else:
            print("Senha incorreta! Acesso negado.")

    elif opcao == "2":
        enem.listar()

    elif opcao == "3":

        senha = input("Digite a senha do professor: ")

        if senha == "1234":
            enem.excluir()
        else:
            print("Senha incorreta! Acesso negado.")

    elif opcao == "4":
        enem.simulado()

    elif opcao == "5":
        enem.ver_historico()

    elif opcao == "6":
        print("Obrigado por utilizar o sistema Personalize!")
        break

    else:
        print("Opção inválida! Tente novamente.")






































































