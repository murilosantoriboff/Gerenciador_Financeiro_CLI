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


def registrar_investimento(mes, dados):
    nome_do_investimento=str(input("Escreva o nome do investimento: "))
    print("-------------------------------------------")
    while True:
        try:
            valor_investimento = float(input("Escreva o valor do investimento: "))
            print("-------------------------------------------")
            print()
            break
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue
    for mes_investimento_total, resultado_investimento_total in dados.items():
        if mes_investimento_total == mes:
            resultado_investimento_total[f"inv-{nome_do_investimento}"] = valor_investimento
            print(dados)
    return dados