import PyPDF2

PDF_FILE = 'assets/Scripture_for_Every_Moment.pdf'

def read_asset(PDF_FILE):
    """
    Read the PDF file and return the text
    """
    file = open(PDF_FILE, 'rb')
    pdf_reader = PyPDF2.PdfReader(file)
    txt = []

    for pages in pdf_reader.pages:
        txt.append(pages.extract_text())
    return txt

def main():
    file = read_asset(PDF_FILE)
    print(file[0:5])

if __name__ == '__main__':
    main()