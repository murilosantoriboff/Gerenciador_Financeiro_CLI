from utils import interface

if __name__ == "__main__":
    dados_usuario = interface.interface_dados_usuario() # Retorna uma lista com os dados do user (Nome, valor e mes)
    dados_mestre = dados_usuario # usar essa variavel para manipular os dados do usuario
    #print(dados_usuario) # Teste para ver os dados e os meses
    opcao_menu = interface.menu_principal()
    #print(opcao_menu)  # Teste para ver se a opção está correta