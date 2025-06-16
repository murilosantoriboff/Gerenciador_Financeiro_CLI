import os

def pedir_mes_despesa():
    os.system('cls')
    while True:
        try:
            print("-------------------------------------------")
            mes_despesa = int(input("Qual mes deseja registrar a despesa: "))
            if 1 <= mes_despesa <= 12:
                return mes_despesa
            else:
                print("Mes invalido, por favor escolha um mes entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")



def registrar_despesa(mes, dados):
    nome_despesa = str(input("Escreva o nome da despesa: "))
    while True:
        try:
            valor_despesa = float(input("Escreva o valor da despesa: "))
            print("-------------------------------------------")
            print()
            break  
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue
    for mes_despesa_total, resultado_despesa_total in dados.items():
        if mes_despesa_total == mes:
            resultado_despesa_total[f"desp-{nome_despesa}"] = valor_despesa
            print("------------------------------------------------------")
            print(f"Despesa de adicionada R${valor_despesa:.2f} ao mês {mes} com sucesso!")
            print("------------------------------------------------------")
    return dados