# output in PDF with an image inserted
from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.set_title('Weather Forecast')
pdf.set_text_color(r=16)

pdf.cell(40, 10, 'weather forecast')
pdf.ln(15)
pdf.image("C:\\Users\\KATTAKART\\Pictures\\23793-9-weather-photos-thumb1.png", x=80, y=25)
pdf.ln(15)
pdf.output('trail7.pdf')
os.system('trail7.pdf')
