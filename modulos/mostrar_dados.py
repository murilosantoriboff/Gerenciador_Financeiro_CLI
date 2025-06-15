import os

def mostrar_dados_user(dados):
    os.system("cls")
    print()
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("Mostrar Dados do Usuario")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    for mes, resultado in dados.items():
        for k, v in resultado.items():
            print(k,v)
            # ver se k == "nome" e k == "valor" ai mostra se nao mostra oq tem nos outros dicts
            if k == "nome" and k == "valor":
                print("Mês:", mes)
                print("Nome cadastrado:", resultado["nome"])
                print("Valor inserido: R$", resultado["valor"])
                print("------------------------------------------")
                print()
                

"""if resultado != {}:
    if resultado["nome"] != "" and resultado["valor"] != "":
        print("Mês:", mes)
        print("Nome cadastrado:", resultado["nome"])
        print("Valor inserido: R$", resultado["valor"])
        print("------------------------------------------")
        print()"""