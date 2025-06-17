import os

def pedir_mes_saque():
    os.system("cls")
    while True:
        try:
            print("-------------------------------------------")
            mes_saque = int(input("Qual mês deseja registrar o saque: "))
            if 1 <= mes_saque <= 12:
                return mes_saque
            else:
                print("Mês inválido, por favor escolha um mês entre 1 e 12.")
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

    nome_pessoa = "Usuário"
    for resultado_para_nome_rel_pdf in dados.values():
        if isinstance(resultado_para_nome_rel_pdf, dict) and "nome" in resultado_para_nome_rel_pdf:
            nome_pessoa = resultado_para_nome_rel_pdf["nome"]

    if mes not in dados:
        dados[mes] = {}

    if "nome" not in dados[mes]:
        dados[mes]["nome"] = nome_pessoa
    else:
        print(f"Nome cadastrado para o mês {mes}: {dados[mes]['nome']}")

    info = dados[mes]
    saldo_valor = info.get("valor", 0)

    if saldo_valor >= valor_saque:
        info["valor"] -= valor_saque
        info[f"saque-{valor_saque}"] = valor_saque
        print("-------------------------------------------")
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso do saldo principal!")
        print("-------------------------------------------")
    else:
        if saldo_valor > 0:
            print("-------------------------------------------")
            print(f"Saldo insuficiente. Só é possível sacar dos investimentos se o saldo principal for zero.")
            print("-------------------------------------------")
            return dados

        saldo_invest = sum(v for k, v in info.items() if k.startswith("invest-"))
        if saldo_invest >= valor_saque:
            restante = valor_saque
            for chave in list(info.keys()):
                if chave.startswith("invest-") and restante > 0:
                    if info[chave] >= restante:
                        info[chave] -= restante
                        restante = 0
                    else:
                        restante -= info[chave]
                        info[chave] = 0

            info[f"saque-{valor_saque}"] = valor_saque
            print("-------------------------------------------")
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso dos investimentos!")
            print("-------------------------------------------")
        else:
            print("-------------------------------------------")
            print(f"Saldo insuficiente. Não é possível sacar R${valor_saque:.2f} no mês {mes}!")
            print("-------------------------------------------")

    return dados
