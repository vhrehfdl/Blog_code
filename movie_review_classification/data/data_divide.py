import csv

'''
[1] 목적
- 데이터를 train set과 validation set으로 나눈다.
'''


def data_divide(input_file, train_file, validation_file, portion):
    file = open(input_file, 'r', encoding='utf-8')
    csvReader = csv.reader(file)

    train_file = open(train_file, 'w', encoding='utf-8', newline='')
    validation_file = open(validation_file, 'w', encoding='utf-8', newline='')

    pos, neg = [], []

    for row in csvReader:
        review, label = row[0], row[1]

        if int(label) == 0:
            pos.append([review, label])

        elif int(label) == 1:
            neg.append([review, label])


    print(len(pos))
    print(len(neg))


    # [2] 긍정 리뷰의 1:9로 train과 validation으로 구분한다.
    for i in range(0, len(pos)):
        if i < len(pos) * portion :
            wr = csv.writer(validation_file)
            wr.writerow([pos[i][0], 1])

        else :
            wr = csv.writer(train_file)
            wr.writerow([pos[i][0], 1])


    # [3] 부정 리뷰의 1:9로 train과 validation으로 구분한다.
    for i in range(0, len(neg)):
        if i < len(neg) * portion:
            wr = csv.writer(validation_file)
            wr.writerow([neg[i][0], 0])

        else:
            wr = csv.writer(train_file)
            wr.writerow([neg[i][0], 0])


data_divide("../data/data_komoran2.csv", "../data/train_komoran2.csv", "../data/validation_komoran2.csv", portion=0.1)
data_divide("../data/data_komoran3.csv", "../data/train_komoran3.csv", "../data/validation_komoran3.csv", portion=0.1)
data_divide("../data/data_komoran4.csv", "../data/train_komoran4.csv", "../data/validation_komoran4.csv", portion=0.1)
data_divide("../data/data_komoran5.csv", "../data/train_komoran5.csv", "../data/validation_komoran5.csv", portion=0.1)