import time;
import numpy as np;
import pandas as panda;
import csv
start_timer = time.time();

# f = open('26.csv', 'r');
# print(*f);
# f.close();
# print("Затрачено: %s секунд" % (time.time()-start_timer))

#вариант 2
# file_path = '26.csv';

# f = panda.read_csv(file_path, delimiter='\t', header=None)
# numpyRead = f.to_numpy();
# print(numpyRead)
# print("Затрачено: %s секунд" % (time.time()-start_timer))

#вариант 3
with open('26.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))
print("Затрачено: %s секунд" % (time.time()-start_timer))