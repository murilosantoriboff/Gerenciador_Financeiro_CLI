from utils import interface
from modulos import investimentos, mostrar_dados, despesas, saques, alteracao, registro_investimento

if __name__ == "__main__":
    dados_usuario = interface.interface_dados_usuario() # Retorna uma lista com os dados do user (Nome, valor e mes)
    dados_mestre = dados_usuario # usar essa variavel para manipular os dados do usuario
    while True:
        opcao_menu = interface.menu_principal()
        if opcao_menu==1:
            mostrar_dados.mostrar_dados_user(dados_mestre)
        elif opcao_menu == 2:
            alteracao_dados = alteracao.adicionar_dados(dados_mestre)
            dados_mestre = alteracao_dados
        elif opcao_menu == 3:
            mes_escolhido_despesa=despesas.pedir_mes_despesa()
            dados_mestre_com_despesas = despesas.registrar_despesa(mes_escolhido_despesa, dados_mestre)
            dados_mestre = dados_mestre_com_despesas
        elif opcao_menu == 4:
            mes_escolhido_investimento=registro_investimento.pedir_mes_investimento()
            dados_mestre_com_investimentos = registro_investimento.registrar_investimento(mes_escolhido_investimento, dados_mestre)
            dados_mestre = dados_mestre_com_investimentos
        elif opcao_menu == 5:
            # Registrar Deposito
            pass
        elif opcao_menu == 6:
            mes_escolhido_saque = saques.pedir_mes_saque()
            dados_mestre_com_saques = saques.registrar_saque(mes_escolhido_saque, dados_mestre)
            dados_mestre = dados_mestre_com_saques
        elif opcao_menu == 7:
            investimentos.simular_investimento()
        elif opcao_menu == 8:
            # Simular Financiamento
            pass
        elif opcao_menu == 9:
            # Murilo - Relatorio Mensal
            pass
        elif opcao_menu == 10:
            # Murilo - Relatorio Mensal PDF
            pass
        elif opcao_menu == 11:
            # Murilo - Relatorio Anual
            pass
        elif opcao_menu == 12:
            # Murilo - Relatorio Anual PDF
            pass
        elif opcao_menu == 13:
            # Murilo - Relatorio Grafico (MatPloit Lib)
            pass
        elif opcao_menu==14:
            print("--------------------")
            print("SAINDO DO APLICATIVO")
            print("--------------------")
            break