import os
import pandas as pd
import numpy as np

from base import DATA_DIR, accuracy_score
from sklearn.model_selection import train_test_split


data = pd.read_csv(os.path.join(DATA_DIR, "final.csv"), skipinitialspace=True)
X = data[['username', 'ranking', 'title', 'comments']]
y = data['useful']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


# In the useful reviews
# 0.5% < 11.0
# 0.5% > 383.90999999999985
len_comments = X_train['comments'].str.len()
# a = len_comments.where(len_comments<100, 'green', 'red')
# print(a)
# print(len_comments)
# print(len_comments.where((len_comments > 11) & (len_comments < 384), '0'))
len_comments = len_comments.where((len_comments < 11) | (len_comments > 384), 1)
predictions = len_comments.where(len_comments == 1, 0)
# print(predictions)
# print(len_comments)
print(accuracy_score(y_train, predictions))
