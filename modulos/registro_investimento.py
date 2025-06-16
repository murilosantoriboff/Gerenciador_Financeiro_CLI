import os

def pedir_mes_investimento():
    os.system("cls")
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
    while True:
        try:
            valor_investimento = float(input("Escreva o valor do investimento: "))
            print("-------------------------------------------")
            print()
            break  
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue
    for mes_inv_total, resultado_inv_total in dados.items():
        if mes_inv_total == mes:
            resultado_inv_total[f"invest-{valor_investimento}"] = valor_investimento
            print("------------------------------------------------------")
            print(f"Investido o valor de R${valor_investimento:.2f} no mês {mes} com sucesso!")
            print("------------------------------------------------------")
    return dados