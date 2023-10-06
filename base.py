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

def rejoin_text(txt):
    """
    Rejoin incomplete Bible verses

    Some bible verses (those that occured around the ending of the page)
    were split into two. This function rejoin those verses.
    """
    new_txt = []
    n = 0
    while n < len(txt):
        try:
            word = txt[n]
            # checks against number that are still in the dataset and wasn't removed
            # print(word, len(word))
            if not word.isdigit():
                if (not word[-1].isdigit() and not word.isupper()):
                    word = txt[n] + txt[n+1]
                    n += 1
                else:
                    pass
                new_txt.append(word)
        except Exception as e:
            print(f"An {e} error occured at {n}, \n {txt[n]}")
        n += 1
    return new_txt
            
def main():
    file = read_asset(PDF_FILE)
    pages = process_text(file)
    pages = rejoin_text(pages)
    print(pages)

if __name__ == '__main__':
    main()