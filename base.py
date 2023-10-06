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

def process_text(txt):
    """
    Process the text and return the text in a list
    """
    whole_text = []
    for page in txt:
        page = page.split('\n \n')
        for text in page[1:]:
            text = text.split(' \n')
            whole_text.extend([
                x.strip(' ') for x in text if (
                    isinstance(x, str) and x != ' '
                    )
                ])
    return whole_text

def main():
    file = read_asset(PDF_FILE)
    pages = process_text(file)
    print(pages)

if __name__ == '__main__':
    main()