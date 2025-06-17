import matplotlib.pyplot as plt
import os

def gerar_grafico_financeiro(dados):
    total_depositos = 0
    total_saques = 0
    total_investimentos = 0
    total_despesas = 0

    for info in dados.values():
        if not isinstance(info, dict):
            continue
        total_depositos += info.get("valor", 0)
        for chave, valor in info.items():
            if chave.startswith("saque-"):
                total_saques += valor
            elif chave.startswith("invest-"):
                total_investimentos += valor
            elif chave.startswith("desp-"):
                total_despesas += valor

    categorias = ["Depósitos", "Saques", "Investimentos", "Despesas"]
    valores = [total_depositos, total_saques, total_investimentos, total_despesas]
    os.system('cls')
    print("-------------------------------------------")
    print("Escolha o tipo de gráfico:")
    print("[1] Gráfico de Barras")
    print("[2] Gráfico de Pizza")
    print("[3] Gráfico de Linha")
    print("-------------------------------------------")

    opcao = input("Digite a opção desejada: ")

    plt.figure(figsize=(8, 6))
    plt.title("Resumo Financeiro Anual")

    if opcao == "1":
        plt.bar(categorias, valores, color=["green", "red", "blue", "orange"])
        plt.ylabel("Valor (R$)")
        plt.xlabel("Categorias")
    elif opcao == "2":
        plt.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=140, colors=["green", "red", "blue", "orange"])
        plt.axis("equal")
    elif opcao == "3":
        plt.plot(categorias, valores, marker="o", linestyle="-", color="purple")
        plt.ylabel("Valor (R$)")
        plt.xlabel("Categorias")
    else:
        print("Opção inválida. Nenhum gráfico será gerado.")
        return

    pasta_graficos = os.path.join(os.getcwd(), "graficos")
    os.makedirs(pasta_graficos, exist_ok=True)

    caminho = os.path.join(pasta_graficos, "grafico_financeiro.png")
    plt.tight_layout()
    plt.savefig(caminho)
    plt.show()