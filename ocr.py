import PyPDF2 as pp

def extract_text(file):
    fileobj = open(file, 'rb')

    # creating a pdf reader object 
    pdfReader = pp.PdfFileReader(fileobj) 
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    fileobj.close() 
    return text

