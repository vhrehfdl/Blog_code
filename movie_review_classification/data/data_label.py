import csv

'''
[1] 목적
=> 데이터 라벨링을 진행한다.
부정은 0 / 긍정은 1로 라벨링한다.

[2] 
'''


def data_label(input_file, output_file):
    file = open(input_file, 'r', encoding='utf-8')
    csvReader = csv.reader(file)

    file_output = open(output_file, 'w', encoding='utf-8', newline='')


    for row in csvReader:
        review, label = row[0], row[1]

        if int(label) < 4:
            wr = csv.writer(file_output)
            wr.writerow([review, 0])

        elif int(label) == 10:
            wr = csv.writer(file_output)
            wr.writerow([review, 1])


data_label("../data/data.csv", "../data/data_label.csv")
