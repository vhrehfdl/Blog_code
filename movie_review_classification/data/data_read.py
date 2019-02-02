import numpy as np
import csv

'''
[1] 목적
review 개수 파악하고 label 비율 파악
'''


def read(filename):
    line_counter = 0

    file_dir = open(filename, 'r', encoding='utf-8')
    csv_reader = csv.reader(file_dir)

    texts, scores = [], []


    for row in csv_reader:
        line_counter += 1

        review, score = row[0], row[1]

        texts.append(review)  # row[0]은 텍스트
        scores.append(score)  # row[1]은 라벨

        if int(score) == 3:
            print(review)


    print("전체 데이터 개수 : " + str(line_counter))
    print("prediction 비율")
    index, count = np.unique(scores, return_counts=True)
    print(index)
    print(count)



# read('../data/train_komoran1.csv')
# read('../data/validation_komoran1.csv')

# read('../data/train_komoran2.csv')
# read('../data/validation_komoran2.csv')
#
read('../data/train_komoran3.csv')
read('../data/validation_komoran3.csv')



