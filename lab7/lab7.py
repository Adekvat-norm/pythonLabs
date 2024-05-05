import csv;
import numpy as np;
import pandas as panda;

# file_path = '26.csv';

# f = panda.read_csv(file_path, delimiter='\t', header=None)
# numpyRead = f.to_numpy();
# mistakes(numpyRead);
# print(numpyRead)


def correct_mistakes(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    def get_replacement_value(index, lines, column_index=2):
        prev_index = index - 1
        next_index = index + 1
        if prev_index >= 0 and lines[prev_index].strip().split(',')[column_index] != '':
            return lines[prev_index].strip().split(',')[column_index]
        elif next_index < len(lines) and lines[next_index].strip().split(',')[column_index] != '':
            return lines[next_index].strip().split(',')[column_index]
        else:
            return '5more'

    with open(file_path, 'w') as file:
        for index, line in enumerate(lines):
            elements = line.strip().split(',')
            if elements[2] == '':
                elements[2] = get_replacement_value(index, lines)
            file.write(','.join(elements) + '\n')

file_path = '26TEST.csv'
correct_mistakes(file_path)




