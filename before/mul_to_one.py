import os
import csv

# Merge all the csv files into one

# Project DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DATA DIR
DATA_DIR = os.path.join(BASE_DIR, 'data')

def get_csv(dir):
    '''
    Return all csv files path inside the given dir

    input: the dir to be searched
    output: a generator contain all valid csv files path
    '''
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                yield os.sep.join([dirpath, filename])

def _all_csv_data(csv_files):
    '''
    Return all data inside the csv files

    input: csv_files: generator contain all the csv files path
    output: return a generator contain all data inside csv_files
    '''
    for c_file in csv_files:
        with open(c_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                yield row

def merge_csv(csv_files):
    with open('fin_final.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in _all_csv_data(csv_files):
            writer.writerow(row)

def main():
    merge_csv(['fin_useful.csv', 'fin_useless.csv'])

if __name__ == '__main__':
    main()

