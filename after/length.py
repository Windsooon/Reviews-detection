import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from comments.base import DATA_DIR

full_data = pd.read_csv(os.path.join(DATA_DIR, 'fin_final.csv'))

useful = full_data['useful']
data_without_useful = full_data.drop('useful', axis = 1)
data_without_useful['lencomments'] = data_without_useful['comments'].str.len()
predictions = [1 if x >= 10 and x <= 465 else 0 for x in data_without_useful['lencomments']]

print('Accuracy score: ', format(accuracy_score(useful, predictions)))
print('Precision score: ', format(precision_score(useful, predictions)))
print('Recall score: ', format(recall_score(useful, predictions)))
print('F1 score: ', format(f1_score(useful, predictions)))
