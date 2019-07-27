import os
import csv
import numpy as np
import sklearn
# from sklearn.naive_bayes import GaussianNB
from comments.base import cut_words, STOP_WORDS, DATA_DIR

def get_reviews_lst():
    # useful = os.path.join(DATA_DIR, 'useful.csv')
    # useless = os.path.join(DATA_DIR, 'useless.csv')
    # for file in useful, useless:
    #     with open(file, newline='') as csvfile:
    #         reader = csv.reader(csvfile, delimiter=',')
    #         for row in reader:
    #             yield row[-1]
    return ['打开198597.cOm注册有活动*E812', '打开198597.cOm注册有活动*E350', '潮流穿搭在nice']

vectorizer = sklearn.feature_extraction.text.CountVectorizer(
    tokenizer=cut_words,
    stop_words=STOP_WORDS)
X = vectorizer.fit_transform(get_reviews_lst())
print(vectorizer.get_feature_names())
print(X.toarray())

# import pkuseg
# seg = pkuseg.pkuseg()           # 以默认配置加载模型
# text = seg.cut('收藏《 RB⑧⑥②①●COM 》好盈球')  # 进行分词
# print(text)
# text = seg.cut('决战美粥杯拿500圆')  # 进行分词
# print(text)
# text = seg.cut('打开198597.cOm注册有活动*E309')  # 进行分词
# print(text)
