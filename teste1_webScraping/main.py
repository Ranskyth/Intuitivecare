import wget as install   # type: ignore
from zipfile import ZipFile
import os

urls = ["https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf","https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"]

files = ["Anexo_I.pdf","Anexo_II.pdf"]
output_pdfs = "PDFs"
output_zip = "Zip"


def installFiles(urls,files):
    for i,url in enumerate(urls):
        install.download(url,f"{output_pdfs}/"+files[i])


def pdfToZip(anexos):
    with ZipFile(f"{output_zip}/Anexos.zip", "w") as zip:
        for file in anexos:
            zip.write(f"{output_pdfs}/{file}")  
           
def main():
    if(not os.path.exists(output_pdfs) and not os.path.exists(output_zip)):
        os.mkdir(f"./{output_pdfs}")
        os.mkdir(f"./{output_zip}")

    installFiles(urls, files)
    pdfToZip(files)
   

if __name__ == '__main__':
    main()