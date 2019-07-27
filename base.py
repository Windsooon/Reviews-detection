import os
import csv
import logging
import numpy as np
import pkuseg

from sklearn.feature_extraction.text import CountVectorizer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'cleaned_data')
STOP_WORDS = ['如果', '但是', '他们', '你们', '并且', '或者', '不只', '而且', '还有', '即使', '接着', '紧接着', '尽管', '例如', '虽然', '同时', '无论', '要么', '以及', '以至', '以至于', '因此', '因为', '由于', '怎样', '这么', '这些', '那些', '只是', '只要', '如此', '对于', '只有', '比如', '不但', '不是', '不能', '不要', '不过', '不再', '差不多', '除此', '除了', '大概', '大约', '何止', '即将', '尽量', '经常', '竟然', '居然', '立刻', '马上', '难道', '偶而', '偶尔', '仍然', '我们', '正在', '一款', '可以', '这里', '找到', '非常', '一个', '按照', '最后', '所以', '以前', '优势', '左右', '这个', '还是', '这次', '相当', '有个', '离开', '不错', '之后', '一样', '一起', '真的', '有点', '敲门', '原本', '于是', '以后', '所有', '甚至', '根本', '哪怕', '中国', '美国', '德国', '法国', '外国', '中华人民共和国', '台湾', '香港', '澳门', '日本', '韩国', '西班牙', '意大利']

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

def accuracy_score(truth, pred):
    '''
    Returns accuracy score for input truth and predictions.
    input: truth: expected value
           pred: prediction value
    '''
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):
        # Calculate and return the accuracy as a percent
        return ("Predictions have an accuracy of {:.2f}%.".
            format((truth == pred).mean()*100))
    else:
        return "Number of predictions does not match number of outcomes!"

def cut_words(sentence):
    seg = pkuseg.pkuseg()
    text = seg.cut(sentence)
    return text
