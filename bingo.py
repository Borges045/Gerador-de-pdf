import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth

# Lista de alimentos bíblicos
alimentos = [
    "trigo", "cevada", "pão sem fermento", "figos", "uvas", "tâmaras",
    "romãs", "amêndoas", "lentilhas", "pepinos", "alho-poró", "cebola",
    "alho", "cordeiro", "cabrito", "peixe", "codornizes", "leite",
    "queijo", "manteiga", "mel", "sal", "canela", "especiarias"
]

# Configurações
total_paginas = 200
itens_por_cartela = 16  # 4x4
cell_size = 120  # tamanho da célula para melhor espaçamento
fonte = "Helvetica-Bold"
fonte_tamanho = 18  # tamanho da fonte dentro das células
titulo_fonte_tamanho = 69
titulo_espacado = "B   I   N   G   O"

# Cores
fundo_cor = colors.HexColor("#f5d098")
texto_cor = colors.black
titulo_cor = colors.HexColor("#183f06")

# Caminho do PDF de saída
pdf_path = "cartelas_final.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)

# Geração das cartelas
for _ in range(total_paginas):
    cartela = random.sample(alimentos, itens_por_cartela)

    # Fundo da página
    c.setFillColor(fundo_cor)
    c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)

    # Título
    c.setFillColor(titulo_cor)
    c.setFont(fonte, titulo_fonte_tamanho)
    c.drawCentredString(A4[0] / 2, A4[1] - 100, titulo_espacado)

    # Configurações para a cartela
    c.setFont(fonte, fonte_tamanho)
    c.setFillColor(texto_cor)
    total_grid_size = cell_size * 4
    start_x = (A4[0] - total_grid_size) / 2
    start_y = A4[1] - 180

    # Monta o grid 4x4
    idx = 0
    for row in range(4):
        for col in range(4):
            x = start_x + col * cell_size
            y = start_y - row * cell_size
            c.rect(x, y - cell_size, cell_size, cell_size, stroke=1, fill=0)

            texto = cartela[idx]
            max_width = cell_size - 10

            if stringWidth(texto, fonte, fonte_tamanho) > max_width:
                partes = texto.split(" ")
                if len(partes) > 1:
                    linha1 = partes[0]
                    linha2 = " ".join(partes[1:])
                    c.drawCentredString(x + cell_size / 2, y - cell_size / 2 + 2, linha1)
                    c.drawCentredString(x + cell_size / 2, y - cell_size / 2 - 14, linha2)
                else:
                    c.setFont(fonte, 14)
                    c.drawCentredString(x + cell_size / 2, y - cell_size / 2 - 6, texto)
                    c.setFont(fonte, fonte_tamanho)
            else:
                c.drawCentredString(x + cell_size / 2, y - cell_size / 2 - 6, texto)

            idx += 1

    c.showPage()

# Salvar o arquivo
c.save()

print(f"PDF salvo como: {pdf_path}")

