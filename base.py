import csv
import logging

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

def get_current_logger(name, filename, filelevel):
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
