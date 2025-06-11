def pedir_mes_investimento():
    print("-------------------------------------------")
    mes_investimento=int(input("Qual mes deseja registrar o investimento: "))
    print("-------------------------------------------")
    return mes_investimento


def registrar_investimento(mes, dados):
    nome_do_investimento=str(input("Escreva o nome do investimento: "))
    print("-------------------------------------------")
    valor_investimento=float(input("Escreva o valor do investimento: "))
    print("-------------------------------------------")
    print()
    for mes_investimento_total, resultado_investimento_total in dados.items():
        if mes_investimento_total == mes:
            resultado_investimento_total[f"inv-{nome_do_investimento}"] = valor_investimento
            print(dados)
    return dados