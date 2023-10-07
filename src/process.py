import PyPDF2
import logging 

logging.basicConfig(
    level=logging.DEBUG,
    filename=".file.log",
    format="%(asctime)s %(funcName)s[%(levelname)s]: %(message)s ",
)
logger = logging.getLogger()

PDF_FILE = 'assets/Scripture_for_Every_Moment.pdf'

def read_asset(PDF_FILE):
    """
    Read the PDF file and return the text
    """
    logger.debug(f"Reading file from {PDF_FILE}...")
    file = open(PDF_FILE, 'rb')
    pdf_reader = PyPDF2.PdfReader(file)
    txt = []
    for pages in pdf_reader.pages:
        txt.append(pages.extract_text())
    logger.debug("All pages retrieved succesfully")
    return txt

def process_text(txt):
    """
    Process the text and return the text in a list
    """
    whole_text = []
    for page in txt:
        page = page.split('\n \n')
        # Each page begins with the title of the book, so 
        # we remove the first item in the list
        for text in page[1:]:
            text = text.split(' \n')
            whole_text.extend([
                x.strip(' ') for x in text if (
                    not x.isdigit() and x != ' ' and x != ''
                    )
                ])
    return whole_text

def join_text(txt, n):
    """
    Join the text into a single string
    """
    if (not word[-1].isdigit() and not word.isupper()):
        logger.debug(f"incomplete verse {word}...")
        word = txt[n] +" "+ txt[n+1]
        logger.debug(f"New verse returned {word}...")
        n += 1
        word, n = join_text(txt, n)
    return word, n

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
            # check if the last character is not a number and word is not in uppercase
            # uppercase words are usually the verse groups 
            word, n = join_text(txt, n)
            # if (not word[-1].isdigit() and not word.isupper()):
            #     logger.debug(f"incomplete verse {word}...")
            #     word = txt[n] +" "+ txt[n+1]
            #     logger.debug(f"New verse returned {word}...")
            #     n += 1
            # else:
            #     pass
            new_txt.append(word)
        except Exception as e:
            logger.error(f"An {e} error occured at {n}, \n {txt[n]}")
        n += 1
    return new_txt

def create_map(txt):
    """
    Create a map of the Bible verses and their corresponding usecase
    """
    bible_map = {}
    NEW_GROUP = False
    KEY = ''
    for verse in txt:
        if verse.isupper():
            KEY = verse.lower()
            bible_map[KEY] = []
        else:
            bible_map[KEY].append(verse)
            NEW_GROUP = False
    return bible_map

def process(pdf_file=PDF_FILE):
    file = read_asset(PDF_FILE)
    logger.debug("File read successfully...")
    pages = process_text(file)
    logger.debug("All pages successfully processed...")
    pages = rejoin_text(pages)
    logger.debug("All incomplete verses fixed...")
    bible_maps = create_map(pages)
    logger.debug("Bible thematic map created successfully...")

    themes = list(bible_maps.keys())
    for theme in themes:
        if len(theme.split()) > 1:
            if theme == "confu sion":
                bible_maps['confusion'] = bible_maps.pop(theme)
            elif theme == "everlasting life":
                bible_maps['eternity'] = bible_maps.pop(theme)
    return bible_maps
    
if __name__ == '__main__':
    process()