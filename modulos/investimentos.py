def pedir_mes_investimento():
    while True:
        try:
            print("-------------------------------------------")
            mes_investimento = int(input("Qual mes deseja registrar o investimento: "))
            if 1 <= mes_investimento <= 12:
                return mes_investimento
            else:
                print("Mes invalido, por favor escolha um mes entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def simular_investimento():
    print("\n=== Simulação de Investimento ===")
    print("Escolha o tipo de investimento:")
    print("1 - CDB (1.33% ao mês)")
    print("2 - Tesouro Selic (1.23% ao mês)")
    print("3 - LCI (0.90% ao mês)")

    tipos = {
        1: ("CDB", 0.0133),
        2: ("Tesouro Selic", 0.0123),
        3: ("LCI", 0.0090)
    }

    try:
        tipo = int(input("Digite a opção (1 a 3): "))
        while tipo not in tipos:
            tipo = int(input("Opção inválida. Escolha entre 1 e 3: "))

        nome_investimento, taxa = tipos[tipo]

        valor_investido = float(input("Digite o valor a investir: R$ "))
        tempo_meses = int(input("Digite o tempo de investimento (em meses): "))

        montante = valor_investido * ((1 + taxa) ** tempo_meses)
        lucro = montante - valor_investido

        print(f"\n--- Resultado da Simulação ({nome_investimento}) ---")
        print(f"Valor investido: R$ {valor_investido:.2f}")
        print(f"Tempo: {tempo_meses} meses")
        print(f"Taxa: {taxa * 100:.2f}% ao mês")
        print(f"Lucro: R$ {lucro:.2f}")
        print(f"Valor final: R$ {montante:.2f}\n")

    except ValueError:
        print("Erro nas entradas. Tente novamente.\n")
        return simular_investimento()
