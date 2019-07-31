import os
import csv
import copy
import logging

from multiprocessing import Pool
from base import write_csv, jaccard_similarity, get_current_logger, DATA_DIR

logger = get_current_logger(__name__, 'simi.log')

class Simi:
    def __init__(self):
        self.lst = []

    def search_simi(self, input):
        start, end, lst = input
        for i in range(start, min(len(lst), end)):
            logger.info('the {0}th data'.format(i))
            for j in range(i+1, len(lst)):
                if jaccard_similarity(lst[i][-1], lst[j][-1]) >= 0.8:
                    logger.info(
                        'we found the {0}th \n {1} \n the {2}th \n {3} quite simi'
                        .format(i, lst[i][-1], j, lst[j][-1]))
                    self.lst[i][3] = '0'
                    self.lst[j][3] = '0'

    def get_all_reviews(self, csv_file):
        '''
        Get all reviews from csv files
        '''
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self.lst.append(row)

    def run(self):
        self.search_simi([0, 10000, self.lst])
        write_csv('answer.csv', self.lst)

s = Simi()
s.get_all_reviews(os.path.join(DATA_DIR, 'useful.csv'))
s.run()
