import os
import csv

def get_useful_comments(csv_file):
    '''
    Get useful comments from csv files
    '''
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|', quotechar='|')
        for row in reader:
            row_lst = row[0].split(',')
            if row_lst[3] == '1':
                yield row_lst

def get_useless_comments(csv_file):
    '''
    Get useless comments from csv files
    '''
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|', quotechar='|')
        for row in reader:
            row_lst = row[0].split(',')
            if row_lst[3] == '0':
                yield row_lst

def write_comments(csv_file, rows):
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            writer.writerow(row)

def main():
    useful_lst = get_useful_comments('useful.csv')
    useless_lst = get_useless_comments('useful.csv')
    write_comments('n_useful.csv', useful_lst)
    write_comments('n_useless.csv', useless_lst)

if __name__ == '__main__':
    main()

