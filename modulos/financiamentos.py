import os

def simular_financiamento():
    os.system('cls')
    print("-------------------------------------------")
    print("Simulação de Financiamento")
    print("1 - Financiamento de Imóvel (1.1% ao mês)")
    print("2 - Financiamento de Veículo (1.38% ao mês)")

    try:
        opcao = int(input("Escolha uma opção de financiamento: "))
        while opcao not in [1, 2]:
            opcao = int(input("Opção inválida. Tente novamente: "))

        valor = float(input("Digite o valor total do financiamento (R$): "))
        meses = int(input("Digite a quantidade de meses para pagar: "))

        if opcao == 1:
            taxa = 0.011  # 1.1% ao mês
            tipo = "Imóvel"
        else:
            taxa = 0.0138  # 1.38% ao mês
            tipo = "Veículo"

        # Fórmula de parcela com juros compostos (Tabela Price)
        parcela = valor * (taxa * (1 + taxa) ** meses) / ((1 + taxa) ** meses - 1)
        total_pago = parcela * meses

        print("\n===== Resultado da Simulação =====")
        print(f"Tipo de financiamento: {tipo}")
        print(f"Valor financiado: R$ {valor:,.2f}")
        print(f"Quantidade de parcelas: {meses}")
        print(f"Valor da parcela: R$ {parcela:,.2f}")
        print(f"Valor total a pagar: R$ {total_pago:,.2f}")
        print("===================================")

    except ValueError:
        print("Entrada inválida. Tente novamente.")
