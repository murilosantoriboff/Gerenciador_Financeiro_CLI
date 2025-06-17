from utils import interface
from modulos import investimentos, mostrar_dados, despesas, saques, alteracao, registro_investimento, relatorios_mensais, relatorios_anuais, pdf_generator, graficos, financiamentos

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
            mes_escolhido_saque = saques.pedir_mes_saque()
            dados_mestre_com_saques = saques.registrar_saque(mes_escolhido_saque, dados_mestre)
            dados_mestre = dados_mestre_com_saques
        elif opcao_menu == 6:
            investimentos.simular_investimento()
        elif opcao_menu == 7:
            financiamentos.simular_financiamento()
        elif opcao_menu == 8:
            mes_relat_mensal = relatorios_mensais.pedir_mes_relatorio_mensal()
            relatorios_mensais.relatorio_mensal(dados_mestre, mes_relat_mensal)
        elif opcao_menu == 9:
            mes_rel_pdf = pdf_generator.pedir_mes_rel_pdf()
            pdf_generator.gerar_relatorio_mensal_pdf(dados_mestre,mes_rel_pdf)
        elif opcao_menu == 10:
            relatorios_anuais.relatorio_anual(dados_mestre)
        elif opcao_menu == 11:
            pdf_generator.gerar_relatorio_anual_pdf(dados_mestre)
        elif opcao_menu == 12:
            graficos.gerar_grafico_financeiro(dados_mestre)
        elif opcao_menu==13:
            print("--------------------")
            print("SAINDO DO APLICATIVO")
            print("--------------------")
            break