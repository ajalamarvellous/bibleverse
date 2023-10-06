import os
import pprint
from io import BytesIO
from urllib.request import urlopen
from process import process
from zipfile import ZipFile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

PDF_FILE = 'assets/Scripture_for_Every_Moment.pdf'
URL = "http://nlp.stanford.edu/data/glove.6B.zip"
embedding_filename = 'glove.6B.200d.txt'
output_file = f"assets/{embedding_filename}.word2vec"

def get_embedding_object():
    if os.path.exists(output_file):
        print("Loading GloVe embedding...")
        glove = KeyedVectors.load_word2vec_format(output_file, binary=False)
        return glove
    
    resp = urlopen(URL)
    print("Downloading GloVe embedding...")
    zipfile = ZipFile(BytesIO(resp.read()))
    print("Opening GloVe embedding...")
    zipfile.extract(embedding_filename)
    print("Extracting GloVe embedding...")
    glove2word2vec(embedding_filename, output_file)
    print("Loading GloVe embedding...")
    os.remove(embedding_filename)
    zipfile.close()
    glove = KeyedVectors.load_word2vec_format(output_file, binary=False)
    return glove

# Path: home.py
def verse_for_theme(feeling=input("How are you feeling? ")):
    bible_map = process(PDF_FILE)
    print("Bible map created...")
    print("One minute, creating embedding...")
    embedding = get_embedding_object()
    print("Embedding created...")
    pprint.pprint(bible_map)

    feeling = feeling.lower().split(' ')
    feeling_embedding = embedding.get_mean_vector(feeling)
    similarity = embedding.distances(feeling_embedding, list(bible_map.keys()))
    idx, l = 0, 1
    for i, s in enumerate(similarity):
        if s < l:
            l = s
            idx = i
    key = list(bible_map.keys())[idx]
    return key

if __name__ == '__main__':
    verses = verse_for_theme()
    print(verses)