def adicionar_dados(dados_mestre):
    try:
        nome = str(input("Digite seu nome: "))
        valor = float(input("Digite o valor: "))
        mes = int(input("Digite o mês para adicionar os dados (1 a 12): "))
        while mes < 1 or mes > 12:
            mes = int(input("Mês inválido! Digite novamente (1 a 12): "))

        if "nome" not in dados_mestre[mes]:
            dados_mestre[mes]["nome"] = nome
        else:

            print(f"Já existe um nome para o mês {mes}: {dados_mestre[mes]['nome']}")

        if "valor" not in dados_mestre[mes]:
            dados_mestre[mes]["valor"] = 0.0

        dados_mestre[mes]["valor"] += valor

        print(f"Adicionado R${valor:.2f} ao mês {mes} com sucesso!")

    except (TypeError, ValueError):
        print("Entrada inválida! Tente novamente.")
        adicionar_dados(dados_mestre)