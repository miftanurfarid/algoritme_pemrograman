import csv

csvfile = open('presensi.csv', newline='')
files = csv.reader(csvfile, delimiter=',')

counter = 0
nama = []

for idx in files:
    if counter == 0:
        print('skip')
    else:
        print(idx)
    counter += 1