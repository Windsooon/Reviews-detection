import os
import pandas as pd
import numpy as np

from comments.base import DATA_DIR
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


data = pd.read_csv(os.path.join(DATA_DIR, "fin_final.csv"), skipinitialspace=True)
X = data[['username', 'ranking', 'title', 'comments']]
y = data['useful']

len_comments = X['comments'].str.len()
predictions = np.ones(len(y))

print('Accuracy score: ', format(accuracy_score(y, predictions)))
print('Precision score: ', format(precision_score(y, predictions)))
print('Recall score: ', format(recall_score(y, predictions)))
print('F1 score: ', format(f1_score(y, predictions)))
