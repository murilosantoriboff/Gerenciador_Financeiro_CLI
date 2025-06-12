def pedir_mes_saque():
    print("-------------------------------------------")
    mes_saque=int(input("Qual mes deseja registrar o saque: "))
    while mes_saque < 1 or mes_saque > 12:
        print("Mes invalido, por favor escolha um mes entre 1 e 12.")
        mes_saque = int(input("Qual mes deseja registrar o saque: "))
    print("-------------------------------------------")
    return mes_saque


def registrar_saque(mes, dados):
    valor_saque=float(input("Escreva o valor do saque: "))
    print("-------------------------------------------")
    print()
    for mes_saque_total, resultado_saque_total in dados.items():
        if mes_saque_total == mes:
            resultado_saque_total[f"saque-{valor_saque}"] = valor_saque 
            print(dados)
    return dados