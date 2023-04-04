from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Coletando o número de tabelas que o usuário deseja criar
n_tabelas = int(input("Digite o número de tabelas que você deseja criar: "))

# Criando uma lista para armazenar as tabelas
tabelas = []

# Loop para criar cada tabela
for i in range(n_tabelas):
    # Coletando o nome da tabela
    nome_tabela = input(f"Digite o nome da tabela {i+1}: ")
    
    # Cabeçalho da tabela de itens
    header = ['Item', 'Quantidade', 'Descrição', 'Preço']

    # Coletando os dados do usuário
    rows = []
    precos = []
    while True:
        item = input("Digite o nome do item (ou deixe em branco para sair): ")
        if not item:
            break
        quantidade = input("Digite a quantidade: ")
        desc = ""
        while True:
            desc_item = input("Digite a descrição do item (ou deixe em branco para finalizar): ")
            if not desc_item:
                break
            desc += "\u2022 " + desc_item + "\n" # Adicionando o bullet point à descrição
        preco = float(input("Digite o preço (exemplo: R$ 10,00): ").replace("R$", "").replace(",", ".")) # Convertendo o preço para float
        rows.append([item, quantidade, desc, preco])
        precos.append(preco)

    # Calculando o valor total
    valor_total = sum(precos)

    # Adicionando os dados da tabela de valor total
    dados_valor_total = [["", "Valor total"], ["", "R$ {:.2f}".format(valor_total)]]

    # Adicionando o cabeçalho na lista de dados da tabela de itens
    data = [header] + rows

    # Criando as tabelas
    table_itens = Table(data)
    table_valor_total = Table(dados_valor_total)

    # Adicionando o nome da tabela como um parágrafo
    estilo_nome_tabela = getSampleStyleSheet()['Heading1']
    nome_tabela_paragrafo = Paragraph(nome_tabela, estilo_nome_tabela)
    
    # Adicionando as tabelas e o nome da tabela à lista de tabelas
    tabelas.append(nome_tabela_paragrafo)
    tabelas.append(table_itens)
    tabelas.append(table_valor_total)

table_style = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey), # Preenchendo o cabeçalho da tabela de itens com cinza
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke), # Mudando a cor do texto do cabeçalho da tabela de itens para branco
    ('ALIGN', (0,0), (-1,0), 'CENTER'), # Alinhando o texto do cabeçalho da tabela de itens para o centro
    ('BACKGROUND', (0,-1), (-1,-1), colors.lightgrey), # Preenchendo a linha do valor total com cinza claro
    ('ALIGN', (-1,-1), (-1,-1), 'RIGHT'), # Alinhando o texto do valor total para a direita
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), # Mudando a fonte do cabeçalho da tabela de itens para negrito
    ('FONTNAME', (0,-1), (0,-1), 'Helvetica-Bold') # Mudando a fonte da coluna de nomes dos itens na tabela de valor total para negrito
])

# Aplicando o estilo nas tabelas
table_itens.setStyle(table_style)
table_valor_total.setStyle(table_style)

# Criando o PDF
pdf = SimpleDocTemplate("orcamento.pdf", pagesize=letter)

# Adicionando as tabelas ao PDF
pdf.build(tabelas)
