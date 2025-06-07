# 💰 Gerenciador Financeiro CLI

Sistema de gerenciamento financeiro via linha de comando (CLI), desenvolvido como parte da disciplina **Introdução à Computação e Suas Tecnologias** – UCS, 2025.

## 👨‍💻 Autores

- Murilo Boff  
- João Vitor Gotz  
- Guilherme Biazzuti  

## 📋 Funcionalidades

- Cadastro e alteração de dados financeiros
- Registro de despesas, ganhos, saques e investimentos
- Simulação de investimentos e financiamentos
- Relatórios mensais e anuais com geração de PDF
- Visualização gráfica de dados com Matplotlib

## 🚀 Tecnologias e Bibliotecas

- Python 3.x
- `matplotlib`
- `fpdf` ou `reportlab`
- `datetime`, `os`, entre outras bibliotecas padrão

## 📁 Estrutura de Pastas

```
gerenciador_financeiro/
│
├── graficos/
├── modulos/
│   ├── alteracao.py
│   ├── cadastro.py
│   └── ...
├── relatorios/
├── utils/
│   ├── calculos_financeiros.py
│   ├── validacoes.py
│   └── ...
├── main.py
├── requirements.txt
└── leame.md
```

## 🛠 Como Rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/gerenciador_financeiro.git
   cd gerenciador_financeiro
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

## 🔒 Observações

- Todos os dados são armazenados localmente, respeitando a LGPD.
- Nenhum dado é enviado para terceiros.
- Funciona offline em qualquer sistema com Python instalado.

---

## 📄 Licença

Este projeto é acadêmico e não possui fins comerciais.  