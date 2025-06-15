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
    for mes_saque_total, resultado_saque_total in dados.items():
        if mes_saque_total == mes:
            resultado_saque_total[f"saque-{valor_saque}"] = valor_saque 
    return dados