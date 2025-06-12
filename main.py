from utils import interface
from modulos import investimentos, mostrar_dados, despesas, saques, alteracao
import os

if __name__ == "__main__":
    dados_usuario = interface.interface_dados_usuario() # Retorna uma lista com os dados do user (Nome, valor e mes)
    dados_mestre = dados_usuario # usar essa variavel para manipular os dados do usuario
    #print(dados_usuario) # Teste para ver os dados e os meses
    
    while True:
        opcao_menu = interface.menu_principal()
        #print(opcao_menu)  # Teste para ver se a opção está correta
        if opcao_menu==1:
            mostrar_dados.mostrar_dados_user(dados_mestre)
        elif opcao_menu == 2:
            alteracao.adicionar_dados(dados_mestre)
        elif opcao_menu == 3:
            mes_escolhido_despesa=despesas.pedir_mes_despesa()
            dados_mestre_com_despesas = despesas.registrar_despesa(mes_escolhido_despesa, dados_mestre)
            dados_mestre = dados_mestre_com_despesas
        elif opcao_menu == 4:
            mes_escolhido_investimento=investimentos.pedir_mes_investimento()
            dados_mestre_com_investimentos = investimentos.registrar_investimento(mes_escolhido_investimento, dados_mestre)
            dados_mestre = dados_mestre_com_investimentos
        elif opcao_menu == 6:
            mes_escolhido_saque = saques.pedir_mes_saque()
            dados_mestre_com_saques = saques.registrar_saque(mes_escolhido_saque, dados_mestre)
            dados_mestre = dados_mestre_com_saques
        elif opcao_menu==14:
            print("--------------------")
            print("SAINDO DO APLICATIVO")
            print("--------------------")
            break