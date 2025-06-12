def mostrar_dados_user(dados):
    for mes, resultado in dados.items():
        if resultado != {}:
            print()
            print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            print("Mostrar Dados do Usuario")
            print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            print("Mês:", mes)
            print("Nome cadastrado:", resultado["nome"])
            print("Valor inserido: R$", resultado["valor"])
            print("------------------------------------------")
            print()