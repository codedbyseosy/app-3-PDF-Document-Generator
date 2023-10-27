from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P") #P is portrait, L is landscape

df = pd.read_csv("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-3/generate_pdfs/topics.csv")

for index, row in df.iterrows():
    pdf.add_page() #used to add pages

    pdf.set_font(family="Times", style="B", size=24) #sets the size of the cell and comes before setting the cell
    pdf.set_text_color(100, 100, 100) #rgb values
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1) #adds methods through cells
    pdf.line(10, 21, 200, 21)



pdf. output("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-3/generate_pdfs/output.pdf") #creates the pdf with the name "output.pdf"