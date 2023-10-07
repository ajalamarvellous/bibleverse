import os
import pprint
import random
import logging
from io import BytesIO
from urllib.request import urlopen
from process import process
from zipfile import ZipFile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

logging.basicConfig(
    level=logging.DEBUG,
    filename=".file.log",
    format="%(asctime)s %(funcName)s[%(levelname)s]: %(message)s ",
)
logger = logging.getLogger()

PDF_FILE = 'assets/Scripture_for_Every_Moment.pdf'
URL = "http://nlp.stanford.edu/data/glove.6B.zip"
embedding_filename = 'glove.6B.200d.txt'
output_file = f"assets/{embedding_filename}.word2vec"

def get_embedding_object():
    if os.path.exists(output_file):
        logger.debug("Loading GloVe embedding...")
        glove = KeyedVectors.load_word2vec_format(output_file, binary=False)
        return glove
    
    resp = urlopen(URL)
    logger.debug("Downloading GloVe embedding...")
    zipfile = ZipFile(BytesIO(resp.read()))
    logger.debug("Opening GloVe embedding...")
    zipfile.extract(embedding_filename)
    logger.debug("Extracting GloVe embedding...")
    glove2word2vec(embedding_filename, output_file)
    logger.debug("Loading GloVe embedding...")
    os.remove(embedding_filename)
    zipfile.close()
    glove = KeyedVectors.load_word2vec_format(output_file, binary=False)
    return glove

# Path: home.py
def verse_for_theme(feeling):
    bible_map = process(PDF_FILE)
    logger.debug(f"Bible map created, the key themes {bible_map.keys()}...")
    embedding = get_embedding_object()
    logger.debug("Embedding created...")
    
    feeling = feeling.lower().split(' ')
    logger.debug("Retrieving embedding for input")
    feeling_embedding = embedding.get_mean_vector(feeling)
    logger.debug("Getting most similar theme to feeling in the map")
    similarity = embedding.distances(feeling_embedding, list(bible_map.keys()))
    idx, l = 0, 1
    for i, s in enumerate(similarity):
        if s < l:
            l = s
            idx = i
    key = list(bible_map.keys())[idx]
    logger.debug(f"Most similar theme retrieved {key}")
    return f"Here is a bible verse for you: {random.choice(bible_map[key])}"

if __name__ == '__main__':
    feeling = input("How are you feeling? ")
    verses = verse_for_theme(feeling)
    logger.debug(verses)