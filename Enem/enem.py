import database


def cadastrar():
    print("\n===== CADASTRAR QUESTÃO =====")

    materia = input("Digite a matéria: ")
    ano = int(input("Digite o ano: "))

    enunciado = input("Digite o enunciado: ")

    print("\nDigite as alternativas:")
    a = input("A) ")
    b = input("B) ")
    c = input("C) ")
    d = input("D) ")
    e = input("E) ")

    resposta = input("\nResposta correta (A/B/C/D/E): ").upper()

    while resposta not in ["A", "B", "C", "D", "E"]:
        print("Resposta inválida!")
        resposta = input("Digite A, B, C, D ou E: ").upper()

    database.cadastrar_questao(
        materia, ano, enunciado, a, b, c, d, e, resposta
    )

    print("\nQuestão cadastrada com sucesso!")


def listar():
    print("\n===== QUESTÕES CADASTRADAS =====")

    questoes = database.listar_questoes()

    if not questoes:
        print("Nenhuma questão cadastrada.")
        return

    for questao in questoes:
        print("\nID:", questao[0])
        print("Matéria:", questao[1])
        print("Ano:", questao[2])
        print("Enunciado:", questao[3])
        print("A)", questao[4])
        print("B)", questao[5])
        print("C)", questao[6])
        print("D)", questao[7])
        print("E)", questao[8])
        print("-----------------------------")


def excluir():
    print("\n===== EXCLUIR QUESTÃO =====")

    listar()

    id_questao = int(input("\nDigite o ID da questão que deseja excluir: "))

    excluida = database.excluir_questao(id_questao)

    if excluida:
        print("Questão excluída com sucesso!")
    else:
        print("Questão não encontrada.")


def simulado():
    print("\n===== SIMULADO ENEM =====")

    nome = input("Digite o nome do aluno: ")

    questoes = database.listar_questoes()

    if not questoes:
        print("Não existem questões cadastradas para o simulado.")
        return

    acertos = 0

    for questao in questoes:

        print("\n================================")
        print("Matéria:", questao[1])
        print("Ano:", questao[2])
        print("\n", questao[3])

        print("\nA)", questao[4])
        print("B)", questao[5])
        print("C)", questao[6])
        print("D)", questao[7])
        print("E)", questao[8])

        resposta = input("\nSua resposta (A/B/C/D/E): ").upper()

        while resposta not in ["A", "B", "C", "D", "E"]:
            print("Resposta inválida!")
            resposta = input("Digite A, B, C, D ou E: ").upper()

        resposta_correta = questao[9]

        if resposta == resposta_correta:
            print("Resposta correta!")
            acertou = 1
            acertos += 1
        else:
            print("Resposta incorreta!")
            print("Resposta correta:", resposta_correta)
            acertou = 0

        database.registrar_resultado(
            nome, questao[0], resposta, acertou
        )

    print("\n================================")
    print("SIMULADO FINALIZADO!")
    print("Aluno:", nome)
    print(f"Você acertou {acertos} de {len(questoes)} questões!")
    print("================================")


def ver_historico():
    print("\n===== HISTÓRICO DE DESEMPENHO =====")

    resultados = database.historico()

    if not resultados:
        print("Nenhum resultado registrado.")
        return

    for resultado in resultados:
        nome = resultado[0]
        total = resultado[1]
        acertos = resultado[2] or 0
        erros = total - acertos

        percentual = (acertos / total) * 100

        print("\nAluno:", nome)
        print("Questões respondidas:", total)
        print("Acertos:", acertos)
        print("Erros:", erros)
        print(f"Aproveitamento: {percentual:.1f}%")
        print("-----------------------------")