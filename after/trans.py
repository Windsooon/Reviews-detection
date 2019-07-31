import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from comments.base import DATA_DIR, cut_words, sigmoid


class Trans:
    def __init__(self):
        self.trans_matrix = pd.read_excel(os.path.join(DATA_DIR, 'trans.xls'), index_col=0)
        # add one to every value
        self.trans_matrix += 1

    def calculate_pro(self, sentence):
        '''
        TODO
        '''
        res = cut_words(sentence, postag=True)
        # Get all the POS
        pos = [r[1] for r in res]
        possibility = 0
        pre = 'begin'
        for i in range(len(pos)-1):
            try:
                possibility += np.log(self.trans_matrix.loc[pre, : ][pos[i]] * 10 / sum(self.trans_matrix.loc[pre, : ]))
            except KeyError:
                pass
            else:
                pre = pos[i]
        return possibility

    def pro(self, csv_file):
        data = pd.read_csv(os.path.join(DATA_DIR, csv_file), skipinitialspace=True)
        data['pro'] = data['comments'].apply(self.calculate_pro)
        data['pro'].to_csv('output_' + csv_file)

    def show(self, csv_file):
        axes = plt.axes()
        axes.set_xlim([-200, 200])
        d = pd.read_csv(csv_file, skipinitialspace=True, names=['pro'])
        plt.hist(d['pro'], color='blue', edgecolor='black', bins = 300)
        plt.title('Log Pro')
        plt.xlabel('log_pro')
        plt.ylabel('number')
        plt.tight_layout()
        plt.show()


t = Trans()
# t.pro('fin_useless.csv')
t.show('output_fin_useless.csv')
