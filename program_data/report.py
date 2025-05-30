from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def txt_to_pdf(txt_file_path, pdf_file_path):
    # ページサイズ設定
    page_width, page_height = A4
    margin = 50
    line_height = 14  # 行の高さ

    c = canvas.Canvas(pdf_file_path, pagesize=A4)
    y = page_height - margin

    with open(txt_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if y < margin:
                c.showPage()  # 新しいページ
                y = page_height - margin
            c.drawString(margin, y, line.strip())
            y -= line_height

    c.save()
    print(f"PDFファイルが作成されました: {pdf_file_path}")

# 使用例
txt_to_pdf("report.txt", "report.pdf")