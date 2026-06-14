from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()

pdf.set_font("Helvetica", style="B", size=22)
pdf.cell(w=0, h=10, text="CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=10, y=50, w=190)

pdf.set_text_color(255, 255, 255)
pdf.set_xy(10, 90)
pdf.cell(w=0, h=50, text=name, align="C")

pdf.output("shirtificate.pdf")