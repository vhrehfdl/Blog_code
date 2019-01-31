import math
import numpy as np


positive_sentence = ["와 이 영화 정말 재미있네요.", "영화가 정말 재미있네요.", "명작 영화 정말 강추합니다."]
negetive_sentence = ["진짜 쓰래기 같은 영화내요", "시간이 아깝습니다.", "이 영화 비추합니다."]
all_sentence = positive_sentence + negetive_sentence
test_sentence = "이 영화 재미있네요."


def Word_Make(sentence_list):

    word = []

    for i in range(0, len(sentence_list)):          # 문장 모음을 문장으로 자른다.
        sentence = sentence_list[i]
        words = sentence.split()

        for j in range(0, len(words)):          # 문장을 단어로 자른다.
            word.append(words[j])

    index, count = np.unique(word, return_counts=True)          # 중복되는 단어의 개수를 구한다.
    word_count = {'index': index, 'count': count, 'word': word}

    return word_count


def Word_Probability(words_list, all_word_counts):

    index, count, word = words_list['index'], words_list['count'], words_list['word']
    word_prob = []

    for i in range(0, len(index)):
        word_prob.append([index[i], (int(count[i]) + 1) / (len(word) + all_word_counts)])

    return word_prob


def classification(sentence, senti_words_list, all_word_counts=None):
    words = []
    score = 0

    for i in range(0, len(sentence.split())):
        words.append(sentence.split()[i])
        flag = True

        for j in range(0, len(senti_words_list)):
            if words[i] == senti_words_list[j][0]:
                score += math.log(float(senti_words_list[j][1]))
                flag = False

        if flag:
            score += math.log(float(1 / (len(senti_words_list[j]) + all_word_counts)))

    score += math.log(float(len(positive_sentence) / len(all_sentence)))

    return score



if __name__ == "__main__":
    all_word = Word_Make(all_sentence)
    pos_word = Word_Make(positive_sentence)
    neg_word = Word_Make(negetive_sentence)


    pos_word_laplace_prob = Word_Probability(pos_word, len(all_word['count']))
    pos_laplace_log_score = classification(test_sentence, pos_word_laplace_prob, len(all_word['count']))
    print(pos_word_laplace_prob)
    print("NB LAPLACE LOG POS SCORE : " + str(pos_laplace_log_score))
    print("\n" * 2)


    neg_word_laplace_prob = Word_Probability(neg_word, len(all_word['count']))
    neg_laplace_log_score = classification(test_sentence, neg_word_laplace_prob, len(all_word['count']))
    print(neg_word_laplace_prob)
    print("NB LAPLACE LOG NEG SCORE : " + str(neg_laplace_log_score))

