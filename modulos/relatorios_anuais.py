import os
def relatorio_anual(dados):
    os.system("cls")
    nomes_meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    for mes_rel_anual, resul_mes_anual in dados.items():
        nome_do_mes_str = nomes_meses.get(mes_rel_anual, f"Mês {mes_rel_anual}")
        print("\n" + "=" * 40)
        print(f"    RELATÓRIO MENSAL - {nome_do_mes_str.upper()}    ")
        print("=" * 40)
        val_saq = 0.0
        val_inv = 0.0
        val_desp = 0.0
        val_tot = 0.0
        for k,v in resul_mes_anual.items():
            if "saque" in k:
                val_saq += v
            if "desp" in k:
                val_desp += v
            if "invest" in k:
                val_inv += v
            if "valor" in k:
                val_tot += v
        print(f"Nome do Registro/Mês: {nome_do_mes_str}")
        print(f"Valor Total: R${val_tot}")
        print(f"Valor Total Despesas: R${val_desp}")
        print(f"Valor Total Investimento: R${val_inv}")
        print(f"Valor Total Saque: R${val_saq}")

        print("=" * 40)
        print("Fim do Relatório\n")