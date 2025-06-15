import os

def mostrar_dados_user(dados):
    os.system("cls")
    print()
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("Mostrar Dados do Usuario")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    for mes, resultado in dados.items():
        if resultado != {}:
            print("Mês:", mes)
            for k, v in resultado.items():
                if k == "nome":
                    print("Nome cadastrado:", v)
                if k == "valor": 
                    print("Valor inserido: R$", v)
                    print("------------------------------------------")
                    print()
                if "invest" in k:
                    print("Valor Investido: R$", v)
                    print("------------------------------------------")
                    print()
                if "desp" in k:
                    print("Despesas: R$", v)
                    print("------------------------------------------")
                    print()