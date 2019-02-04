import xgboost
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm, ensemble
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas




def Load_Data(all_sentence, train_sentence, train_label, valid_texts, valid_labels):
    all_texts = all_sentence

    # 전체, 학습, 검증 데이터 프레임 미리 만들어둔다.
    dfAll, dfTrain, dfValid = pandas.DataFrame(), pandas.DataFrame(), pandas.DataFrame()
    dfAll['text'] = all_texts
    dfTrain['text'], dfTrain['label'] = train_sentence, train_label
    dfValid['text'], dfValid['label'] = valid_texts, valid_labels

    # 라벨링을 해준다.
    encoder = preprocessing.LabelEncoder()
    train_y, valid_y = encoder.fit_transform(dfTrain['label']), encoder.fit_transform(dfValid['label'])

    DataSet = {'train_text': dfTrain['text'], 'valid_text': dfValid['text'], 'train_label': train_y, 'valid_label': valid_y, 'all_text_data': dfAll['text']}

    return DataSet



'''
[2] Convert_Text_To_Vector
'''
def Convert_Text_To_Vector(DataSet):

    AllTextData = DataSet['all_text_data']
    train_text = DataSet['train_text']
    valid_text = DataSet['valid_text']

    # BOW
    count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
    count_vect.fit(AllTextData)
    train_count = count_vect.transform(train_text)

    print(count_vect.vocabulary_)
    print(count_vect.transform(AllTextData).toarray())

    valid_count = count_vect.transform(valid_text)

    TextToVec_DataSet = {'train_count': train_count, 'valid_count': valid_count}

    return TextToVec_DataSet



'''
[3] Train_Model
'''
def Train_Model(classifier, data_set, text_to_vector_data_set, target_names=['0', '1']):

    train_count, train_label = text_to_vector_data_set['train_count'], data_set['train_label']
    valid_count, valid_label = text_to_vector_data_set['valid_count'], data_set['valid_label']


    # train_count와 train_label로 학습해서 모델 생성.
    classifier.fit(train_count, train_label)

    # 학습된 모델에 valid_count를 넣어 정답 예측하기.
    predictions = classifier.predict(valid_count)


    print(predictions)

    return metrics.accuracy_score(predictions, valid_label)





if __name__ == "__main__":
    positive_sentence = ["와 이 영화 정말 재미있네요.", "영화가 정말 재미있네요.", "명작 영화 정말 강추합니다."]
    negetive_sentence = ["진짜 쓰래기 같은 영화내요", "시간이 아깝습니다.", "이 영화 비추합니다."]

    test_sentence = ["영화 재미있네요.", "진짜 비추합니다."]
    test_sentence_label = [0, 1]

    all_sentence = positive_sentence + negetive_sentence + test_sentence

    train_sentence = positive_sentence + negetive_sentence
    train_sentence_label = [0, 0, 0, 1, 1, 1]


    DataSet = Load_Data(all_sentence, train_sentence, train_sentence_label, test_sentence, test_sentence_label)
    TextToVec_DataSet = Convert_Text_To_Vector(DataSet)
    classifier = ensemble.RandomForestClassifier()
    accuracy = Train_Model(classifier, DataSet, TextToVec_DataSet)

    print("모델 정확도: ", accuracy)