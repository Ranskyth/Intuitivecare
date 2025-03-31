from zipfile import ZipFile
import tabula
import os

pageStart = 3
pageEnd = 181

def extract():
    with ZipFile("Zip/Anexos.zip","r") as file:
        file.extract("PDFs/Anexo_I.pdf")

def readFile():
    pdfs = tabula.read_pdf("PDFs/Anexo_I.pdf", pages=f"{pageStart}-{pageEnd}", multiple_tables=True)
    isHeader = False
    for pdf in pdfs:
        pdf.rename(columns={pdf.columns[1]:"RN(alteração)",pdf.columns[3]:"Seg. Odontológica",pdf.columns[4]:"Seg. Ambulatorial"},inplace=True)
 
        if not isHeader:
            pdf.to_csv("dados.csv", mode='a', index=False)
            isHeader=True
        else:
            pdf.to_csv("dados.csv", header=False, mode='a', index=False)

def compact():
    with ZipFile("Teste_GabrielLimaSantana.zip", 'w') as comp:
        comp.write("dados.csv")

def main():
    extract()
    readFile()
    compact()


main()