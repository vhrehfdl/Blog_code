import csv
from konlpy.tag import Komoran

'''
[1] 목적
- 데이터를 train set과 validation set으로 나눈다.
'''


def data_divide(input_file, output_file):
    file = open(input_file, 'r', encoding='utf-8')
    csvReader = csv.reader(file)

    output_file = open(output_file, 'w', encoding='utf-8', newline='')

    data = []

    for row in csvReader:
        review, label = row[0], row[1]
        data.append([review, label])


    komo = Komoran()

    # texts = komo.morphs(data[3][0])
    # texts = komo.pos(data[3][0])
    # print(texts[1][1])

    for i in range(0, len(data)):
        try:
            texts = komo.pos(data[i][0])
            sentence = ""

            print(i)

            for j in range(0, len(texts)):
                # if texts[j][1] == "NNG" or texts[j][1] == "NNP" or texts[j][1] == "NP" or texts[j][1] == "NR" or texts[j][1] == "VV" or texts[j][1] == "VA" or texts[j][1] == "VCN" or texts[j][1] == "VCP":
                if texts[j][1] == "NNG" or texts[j][1] == "NNP":
                # if texts[j][1] == "VV" or texts[j][1] == "VA":

                    if len(texts[j][0]) > 2 :
                        sentence = sentence + " " + texts[j][0]

            wr = csv.writer(output_file)
            wr.writerow([sentence, data[i][1]])


        except:
            i += 1



data_divide("../data/data_label.csv", "../data/data_komoran5.csv")