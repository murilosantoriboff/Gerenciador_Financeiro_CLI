#Funções que editam ou removem registros já existentes
def adicionar_dados(dados_mestre):
    valor = float(input("Digite o valor: "))
    mes = int(input("\nInsira o mês desejado para receber o valor EX(06 => Junho): "))
    while mes<1 or mes>12:
            mes=int(input("Tente Novamente!! Digite o mês desejado EX(06 => Junho): "))
    
    dados_mestre[mes]["valor"] += valor

    print(f"\nValor de R$ {valor:.2f} adicionado com sucesso para o mês {mes}!\n")