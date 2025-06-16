from fpdf import FPDF
import os

class PDFComTabela(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, "Gerenciador Financeiro CLI - UCS - Introdução à Computação e suas Tecnologias", 0, 0, "C")

def pedir_mes_rel_pdf():
    os.system("cls")
    while True:
        try:
            print("-------------------------------------------")
            mes_saque = int(input("Qual mes deseja gerar relatório em PDF: "))
            if 1 <= mes_saque <= 12:
                return mes_saque
            else:
                print("Mes invalido, por favor escolha um mes entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def gerar_relatorio_mensal_pdf(dados, mes):
    for mes_tot_rel_pdf, resul_tot_rel_pdf in dados.items():
        if mes_tot_rel_pdf == mes:
            if resul_tot_rel_pdf == {}:
                print("Mes Invalido! Escolha um mes com dados corretos!")
                print("-------------------------------------------")
                print()
                break
    else:
        info = dados.get(mes, {})
        nome = "Usuário Desconhecido"
        for resultado_para_nome_rel_pdf in dados.values():
            if isinstance(resultado_para_nome_rel_pdf, dict) and "nome" in resultado_para_nome_rel_pdf:
                nome = resultado_para_nome_rel_pdf["nome"]

        nomes_meses = {
            1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
            5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
            9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
        }

        nome_do_mes_str = nomes_meses.get(mes, f"Mês {mes}")

        pdf = PDFComTabela()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, f"Relatório Financeiro - {nome_do_mes_str}", ln=True, align="C")

        pdf.set_font("Arial", "", 12)
        pdf.ln(10)
        pdf.cell(0, 10, f"Usuário: {nome}", ln=True)
        pdf.ln(5)

        total_depositos = info.get("valor", 0)
        total_saques = 0
        total_invest = 0
        total_despesas = 0

        for chave, valor in info.items():
            if chave.startswith("saque-"):
                total_saques += valor
            elif chave.startswith("invest-"):
                total_invest += valor
            elif chave.startswith("desp-"):
                total_despesas += valor

        valor_inicial_bruto = total_depositos + total_saques + total_invest + total_despesas

        pdf.cell(0, 10, f"Valor Inicial Bruto (antes dos descontos): R$ {valor_inicial_bruto:.2f}", ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(50, 10, "Tipo", 1)
        pdf.cell(80, 10, "Categoria/Descrição", 1)
        pdf.cell(40, 10, "Valor (R$)", 1, ln=True)

        pdf.set_font("Arial", "", 12)
        if total_depositos > 0:
            pdf.cell(50, 10, "Valor Atual", 1)
            pdf.cell(80, 10, "valor", 1)
            pdf.cell(40, 10, f"{total_depositos:.2f}", 1, ln=True)

        for chave, valor in info.items():
            if chave.startswith("saque-"):
                pdf.cell(50, 10, "Saque", 1)
                pdf.cell(80, 10, chave, 1)
                pdf.cell(40, 10, f"{valor:.2f}", 1, ln=True)
            elif chave.startswith("invest-"):
                pdf.cell(50, 10, "Investimento", 1)
                pdf.cell(80, 10, chave, 1)
                pdf.cell(40, 10, f"{valor:.2f}", 1, ln=True)
            elif chave.startswith("desp-"):
                pdf.cell(50, 10, "Despesa", 1)
                pdf.cell(80, 10, chave, 1)
                pdf.cell(40, 10, f"{valor:.2f}", 1, ln=True)

        pdf.set_font("Arial", "B", 12)
        pdf.ln(5)
        pdf.cell(0, 10, f"Total de Valor Atual: R$ {total_depositos:.2f}", ln=True)
        pdf.cell(0, 10, f"Total de Saques: R$ {total_saques:.2f}", ln=True)
        pdf.cell(0, 10, f"Total de Investimentos: R$ {total_invest:.2f}", ln=True)
        pdf.cell(0, 10, f"Total de Despesas: R$ {total_despesas:.2f}", ln=True)

        caminho_relatorios = os.path.join(os.getcwd(), "relatorios")
        os.makedirs(caminho_relatorios, exist_ok=True)

        nome_arquivo = f"relatorio_{nome_do_mes_str.lower()}.pdf"
        caminho_arquivo = os.path.join(caminho_relatorios, nome_arquivo)

        pdf.output(caminho_arquivo)
        print("=" * 40)
        print("Relatorio gerado com sucesso!")
        print("=" * 40)


def gerar_relatorio_anual_pdf(dados):
    os.system("cls")
    nomes_meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    pdf = PDFComTabela()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Relatório Financeiro Anual", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(30, 10, "Mês", 1)
    pdf.cell(40, 10, "Tipo", 1)
    pdf.cell(80, 10, "Categoria/Descrição", 1)
    pdf.cell(30, 10, "Valor (R$)", 1, ln=True)

    pdf.set_font("Arial", "", 12)

    total_depositos = 0
    total_saques = 0
    total_invest = 0
    total_despesas = 0

    for mes, info in dados.items():
        nome_mes = nomes_meses.get(mes, f"Mês {mes}")
        if not info:
            continue

        deposito = info.get("valor", 0)
        if deposito > 0:
            pdf.cell(30, 10, nome_mes, 1)
            pdf.cell(40, 10, "Depósito", 1)
            pdf.cell(80, 10, "valor", 1)
            pdf.cell(30, 10, f"{deposito:.2f}", 1, ln=True)
            total_depositos += deposito

        for chave, valor in info.items():
            if chave.startswith("saque-"):
                total_saques += valor
                pdf.cell(30, 10, nome_mes, 1)
                pdf.cell(40, 10, "Saque", 1)
                pdf.cell(80, 10, chave, 1)
                pdf.cell(30, 10, f"{valor:.2f}", 1, ln=True)
            elif chave.startswith("invest-"):
                total_invest += valor
                pdf.cell(30, 10, nome_mes, 1)
                pdf.cell(40, 10, "Investimento", 1)
                pdf.cell(80, 10, chave, 1)
                pdf.cell(30, 10, f"{valor:.2f}", 1, ln=True)
            elif chave.startswith("desp-"):
                total_despesas += valor
                pdf.cell(30, 10, nome_mes, 1)
                pdf.cell(40, 10, "Despesa", 1)
                pdf.cell(80, 10, chave, 1)
                pdf.cell(30, 10, f"{valor:.2f}", 1, ln=True)

    valor_bruto_total_anual = total_depositos + total_saques + total_invest + total_despesas

    pdf.set_font("Arial", "B", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Valor Inicial Bruto Anual (antes dos descontos): R$ {valor_bruto_total_anual:.2f}", ln=True)
    pdf.cell(0, 10, f"Total de Valor: R$ {total_depositos:.2f}", ln=True)
    pdf.cell(0, 10, f"Total de Saques: R$ {total_saques:.2f}", ln=True)
    pdf.cell(0, 10, f"Total de Investimentos: R$ {total_invest:.2f}", ln=True)
    pdf.cell(0, 10, f"Total de Despesas: R$ {total_despesas:.2f}", ln=True)

    caminho_relatorios = os.path.join(os.getcwd(), "relatorios")
    os.makedirs(caminho_relatorios, exist_ok=True)

    nome_arquivo = "relatorio_anual.pdf"
    caminho_arquivo = os.path.join(caminho_relatorios, nome_arquivo)

    pdf.output(caminho_arquivo)
    print("=" * 40)
    print("Relatorio gerado com sucesso!")
    print("=" * 40)