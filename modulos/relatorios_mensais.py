import os

def pedir_mes_relatorio_mensal():  
    os.system("cls")
    while True:
        try:
            print("-------------------------------------------")
            mes_saque = int(input("Qual mes deseja ver o relatório: "))
            if 1 <= mes_saque <= 12:
                return mes_saque
            else:
                print("Mes invalido, por favor escolha um mes entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def relatorio_mensal(dados, mes_escolhido):
    nomes_meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    nome_do_mes_str = nomes_meses.get(mes_escolhido, f"Mês {mes_escolhido}")
    if mes_escolhido not in dados or not dados[mes_escolhido]:
        print(f"Nenhum dado encontrado para o mês de {nome_do_mes_str}.")
        print("=" * 40)
        
    else:
        dados_do_mes = dados[mes_escolhido]

        print("\n" + "=" * 40)
        print(f"    RELATÓRIO MENSAL - {nome_do_mes_str.upper()}    ")
        print("=" * 40)
        val_saq = 0.0
        val_inv = 0.0
        val_desp = 0.0
        for k,v in dados_do_mes.items():
            if "saque" in k:
                val_saq += v
            if "desp" in k:
                val_desp += v
            if "invest" in k:
                val_inv += v
        print(f"Nome do Registro/Mês: {nome_do_mes_str}")
        print(f"Valor Total: R${dados_do_mes["valor"]}")
        print(f"Valor Total Despesas: R${val_desp}")
        print(f"Valor Total Investimento: R${val_inv}")
        print(f"Valor Total Saque: R${val_saq}")

        print("=" * 40)
        print("Fim do Relatório\n")