import fitz
import pathlib

def PDFMerger(count, path, name):
    if count == 1:
        doctotal = fitz.open()
        doc = fitz.open(path+str(count)+".pdf")
        doctotal.insert_pdf(doc)
        doctotal.save(path+name+".pdf")
        doc.close()
        doctotal.close()
    else:
        doctotal = fitz.open(path+name+".pdf")
        doc = fitz.open(path+str(count)+".pdf")
        doctotal.insert_pdf(doc)
        doctotal.save(path+name+".pdf", incremental=True, encryption=0)
        doc.close()
        doctotal.close()
    


name = input("Name: ")
path = str(pathlib.Path(__file__).parent.resolve())+"//PDF//"
number = input("Number: ")

for i in range(1, int(number)+1):
    PDFMerger(i, path, name)