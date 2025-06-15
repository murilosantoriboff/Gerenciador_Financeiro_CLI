import os
def interface_dados_usuario():
    dados = {i: {} for i in range(1, 13)}
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("Bem vindo ao Gerenciador Financeiro CLI")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    try:
        nome=str(input("Digite seu nome: "))
        valor=float(input("Digite o valor: "))
        mes=int(input("Digite o mês para gerir EX(06 => Junho): "))
        while mes<1 or mes>12:
            mes=int(input("Tente Novamente!! Digite o mês para gerir EX(06 => Junho): "))
        dados[mes]["nome"] = nome
        dados[mes]["valor"] = valor
    except (TypeError, ValueError):
        print("------------------------------------------")
        print("Tente Novamente com entradas corretas!! ")
        return interface_dados_usuario()
    return dados

def menu_principal():
    print("*=*=*=*=*=*=*=*=*=")
    print("Menu Principal")
    print("*=*=*=*=*=*=*=*=*=")
    print('1 - Ver seus Dados Financeiros')
    print('2 - Registrar Deposito')
    print('3 - Registrar Despesas')
    print('4 - Registrar Investimento')
    print('5 - Registrar Saque')
    print('6 - Simular Investimento')
    print('7 - Simular Financiamento')
    print('8 - Relatorio Mensal')
    print('9 - Relatorio Mensal em PDF')
    print('10 - Relatorio Anual')
    print('11 - Relatorio Anual em PDF')
    print('12 - Relatorio Grafico')
    print('13 - Sair')
    try:
        opcao = int(input("Escolha uma Opcao: "))
        while opcao < 1 or opcao >13:
            opcao = int(input("Escolha uma Opcao valida: "))
    except (TypeError, ValueError):
        print("------------------------------------------")
        print("Tente Novamente com entradas corretas!! ")
        return menu_principal()
    return opcao