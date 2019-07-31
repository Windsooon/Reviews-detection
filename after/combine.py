import os
import csv
import pickle
import pandas as pd
import numpy as np
import sklearn

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import MultinomialNB
from comments.base import cut_words, STOP_WORDS, DATA_DIR

# Access all data from csv file
df = pd.read_csv(os.path.join(DATA_DIR, 'fin_final.csv'), skipinitialspace=True)
X = df['comments']
y = df['useful']

kf = KFold(n_splits=10, random_state=42, shuffle=True)
accuracies, precisions, recalls, f1s = [], [], [], []

for train_index, test_index in kf.split(X):
    X_train = X[train_index]
    y_train = y[train_index]

    X_test = X[test_index]
    y_test = y[test_index]

    vectorizer = sklearn.feature_extraction.text.CountVectorizer(
        tokenizer=cut_words,
        stop_words=STOP_WORDS)

    training_data = vectorizer.fit_transform(X_train)
    testing_data = vectorizer.transform(X_test)
    naive_bayes = MultinomialNB()
    naive_bayes.fit(training_data, y_train)
    preds = naive_bayes.predict(testing_data)
    len_comments = X_test.str.len()
    bool_comments = [True if x >= 10 and x <= 465 else False for x in len_comments]
    hybrid_preds = np.where(bool_comments, preds, np.zeros(len(preds)))

    accuracies.append(accuracy_score(y_test, hybrid_preds))
    precisions.append(precision_score(y_test, hybrid_preds))
    recalls.append(recall_score(y_test, hybrid_preds))
    f1s.append(f1_score(y_test, hybrid_preds))

average_accuracy = np.mean(accuracies)
average_precision = np.mean(precisions)
average_recall = np.mean(recalls)
average_f1 = np.mean(f1s)
print(average_accuracy)
print(average_precision)
print(average_recall)
print(average_f1)
