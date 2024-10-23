import pandas as pd

# Excelファイルのパス
excel_file_path = "profit_plan.xlsx"

# Excelファイルを読み込む
df = pd.read_excel(excel_file_path)

# DataFrameをHTMLに変換
html_table = df.to_html(index=False)

# HTMLファイルに保存
html_file_path = 'output.html'
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_table)

print(f"HTML table has been saved to {html_file_path}")
