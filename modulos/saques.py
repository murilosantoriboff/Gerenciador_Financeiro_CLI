import os

def pedir_mes_saque():
    os.system("cls")
    while True:
        try:
            print("-------------------------------------------")
            mes_saque = int(input("Qual mes deseja registrar o saque: "))
            if 1 <= mes_saque <= 12:
                return mes_saque
            else:
                print("Mes invalido, por favor escolha um mes entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def registrar_saque(mes, dados):
    while True:
        try:
            valor_saque = float(input("Escreva o valor do saque: "))
            print("-------------------------------------------")
            print()
            break  
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue
    for mes_user_saque, resultado_user_saque in dados.items():
            if resultado_user_saque != {}:
                nome_pessoa = resultado_user_saque["nome"]
    for mes_saque_total, resultado_saque_total in dados.items():
        if mes_saque_total == mes:
            if "nome" not in dados[mes]:
                dados[mes]["nome"] = nome_pessoa
            else:
                print(f"Nome cadastrado para o mês {mes}: {dados[mes]['nome']}")
            if "valor" not in dados[mes]:
                print("-------------------------------------------")
                print(f"Não é possivel saquar R${valor_saque:.2f} ao mês {mes}!")
                print("-------------------------------------------")
                break

            if dados[mes]["valor"] - valor_saque <0:
                print("-------------------------------------------")
                print(f"Não é possivel saquar R${valor_saque:.2f} ao mês {mes}!")
                print("-------------------------------------------")
                break
            dados[mes]["valor"] -= valor_saque
            resultado_saque_total[f"saque-{valor_saque}"] = valor_saque
            print("-------------------------------------------")
            print(f"Retirado R${valor_saque:.2f} ao mês {mes} com sucesso!")
            print("-------------------------------------------")
    return dados