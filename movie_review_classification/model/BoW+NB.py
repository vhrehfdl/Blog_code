from sklearn import preprocessing, naive_bayes, metrics
from sklearn.feature_extraction.text import CountVectorizer
import pandas
import csv
from sklearn.metrics import classification_report


def Load_Data(train_file_dir, validation_file_dir):
    train_file = open(train_file_dir, 'r', encoding='utf-8')            # 학습 데이터 파일 읽기
    csv_reader_train = csv.reader(train_file)

    valid_file = open(validation_file_dir, 'r', encoding='utf-8')       # 검증 데이터 파일 읽기
    csv_reader_valid = csv.reader(valid_file)

    all_texts = []
    train_texts, train_labels = [], []
    valid_texts, valid_labels = [], []

    for row in csv_reader_train:
        all_texts.append(row[0])
        train_texts.append(row[0])
        train_labels.append(row[1])

    train_file.close()

    for row in csv_reader_valid:
        all_texts.append(row[0])
        valid_texts.append(row[0])
        valid_labels.append(row[1])

    valid_file.close()

    # 전체, 학습, 검증 데이터 프레임 미리 만들어둔다.
    dfAll, dfTrain, dfValid = pandas.DataFrame(), pandas.DataFrame(), pandas.DataFrame()
    dfAll['text'] = all_texts
    dfTrain['text'], dfTrain['label'] = train_texts, train_labels
    dfValid['text'], dfValid['label'] = valid_texts, valid_labels

    # 라벨링을 해준다.
    encoder = preprocessing.LabelEncoder()
    train_y, valid_y = encoder.fit_transform(dfTrain['label']), encoder.fit_transform(dfValid['label'])

    DataSet = {'train_text': dfTrain['text'], 'valid_text': dfValid['text'], 'train_label': train_y, 'valid_label': valid_y, 'all_text_data': dfAll['text']}

    return DataSet



def Convert_Text_To_Vector(DataSet):

    AllTextData = DataSet['all_text_data']
    train_text = DataSet['train_text']
    valid_text = DataSet['valid_text']

    word_index, embedding_matrix = None, None           # Word Embedding 일 사용 할 경우에만 사용한다.


    # 문장을 단어로 잘라준다.
    count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
    count_vect.fit(AllTextData)

    train_count = count_vect.transform(train_text)
    print(train_count.shape)

    valid_count = count_vect.transform(valid_text)
    print(valid_count.shape)

    TextToVec_DataSet = {'train_count': train_count, 'valid_count': valid_count, 'word_index': word_index, 'embedding_matrix': embedding_matrix }

    return TextToVec_DataSet



def Train_Model(classifier, data_set, text_to_vector_data_set, target_names=['0', '1']):

    train_count, train_label = text_to_vector_data_set['train_count'], data_set['train_label']
    valid_count, valid_label = text_to_vector_data_set['valid_count'], data_set['valid_label']

    # train_count와 train_label로 분류 model 생성.
    classifier.fit(train_count, train_label)

    # 위에서 만든 model에 검증 데이터 ( valid_count )를 넣어서 분류한다.
    predictions = classifier.predict(valid_count)

    print("-" * 33)
    print(classification_report(valid_label, predictions, target_names=target_names))

    return metrics.accuracy_score(predictions, valid_label)





if __name__ == "__main__":
    DataSet = Load_Data("../data/train.csv", "../data/validation.csv")          # 1. 학습데이터와 검증데이터를 불러온다.
    TextToVec_DataSet = Convert_Text_To_Vector(DataSet)                         # 2. 불러온 Text 데이터를 Vector로 변환해준다.
    classifier = naive_bayes.MultinomialNB()                                    # 3. MultinomialNB를 사용해 분류 model을 만든다.
    # classifier = naive_bayes.BaseNB()
    # classifier = naive_bayes.GaussianNB()
    # classifier = naive_bayes.BernoulliNB()
    accuracy = Train_Model(classifier, DataSet, TextToVec_DataSet)

    print("모델 정확도: ", accuracy)
    print("-" * 33)