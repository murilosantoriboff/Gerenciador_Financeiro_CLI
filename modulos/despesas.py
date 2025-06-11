def pedir_mes_despesa():
    print("-------------------------------------------")
    mes_despesa=int(input("Qual mes deseja registrar a despesa: "))
    print("-------------------------------------------")
    return mes_despesa


def registrar_despesa(mes, dados):
    nome_despesa=str(input("Escreva o nome da despesa: "))
    print("-------------------------------------------")
    valor_despesa=float(input("Escreva o valor da despesa: "))
    print("-------------------------------------------")
    print()
    for mes_despesa_total, resultado_despesa_total in dados.items():
        if mes_despesa_total == mes:
            resultado_despesa_total[f"desp-{nome_despesa}"] = valor_despesa
            
    return dados


            
                