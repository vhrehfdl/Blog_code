import csv
from konlpy.tag import Komoran

'''
[1] 목적
- 데이터를 train set과 validation set으로 나눈다.
'''


def data_small(input_file, output_file):
    file = open(input_file, 'r', encoding='utf-8')
    csvReader = csv.reader(file)

    output_file = open(output_file, 'w', encoding='utf-8', newline='')

    data = []

    for row in csvReader:
        review, label = row[0], row[1]
        data.append([review, label])


    pos, neg = 0,0

    for i in range(0, len(data)):

        if data[i][1] == "1":
            pos += 1

            if pos < 10001:
                wr = csv.writer(output_file)
                wr.writerow([data[i][0], data[i][1]])


        elif data[i][1] == "0":
            neg += 1

            if neg < 10001:
                wr = csv.writer(output_file)
                wr.writerow([data[i][0], data[i][1]])


data_small("../data/train.csv", "../data/train_small.csv")