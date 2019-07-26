import os
import csv
import logging
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'cleaned_data')

def write_csv(csv_file, rows):
    '''
    Write rows to csv_file

    input: csv_file: the name of the file to be written, should end with .csv
           rows: a list contain all the row data
    output: None
    '''
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

def get_current_logger(name, filename, filelevel=logging.WARNING):
    '''
    Return a logger object base on input settings

    input: name: the __name__ from the file
           filename: the filename for the FileHandler
           filelevel: the log level for the FileHandler
    output: logger object
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(filename)
    fh.setLevel(filelevel)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    s1, s2 = add_space(s1), add_space(s2)
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    numerator = np.sum(np.min(vectors, axis=0))
    denominator = np.sum(np.max(vectors, axis=0))
    return numerator / denominator
