from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False , margin=0)

df = pd.read_csv("topics.csv")

for index, item in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=item['Topic'], align='L', ln=1, border=0)
    pdf.line(10,21,200,21)

    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=item['Topic'], align='R', ln=1, border=0)

    page_num = int(item['Pages'])
    for x in range(page_num - 1):
        pdf.add_page()
        pdf.ln(260 + 12)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=item['Topic'], align='R', ln=1, border=0)
    print(item['Topic'])
    print(item['Pages'])

pdf.output("output.pdf")


