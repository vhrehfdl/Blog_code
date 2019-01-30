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


def Word_Probability(pos_word):

    index, count, word = pos_word['index'], pos_word['count'], pos_word['word']
    word_prob = []

    for i in range(0, len(index)):
        word_prob.append([index[i], count[i]/len(word)])            # 각 단어별 확률을 구한다.

    return word_prob


def Classification(sentence, senti_words_list):
    words = []
    score = 1
    score = float(score)

    for i in range(0, len(sentence.split())):
        words.append(sentence.split()[i])
        flag = True

        for j in range(0, len(senti_words_list)):
            if words[i] == senti_words_list[j][0]:
                score *= float(senti_words_list[j][1])
                flag = False

        if flag:
            score *= float(0 / len(senti_words_list[j]))            # 언급 되지 않은 단어 값 계산


    score = float(len(positive_sentence) / len(all_sentence)) * score           # 최종 계산

    return score



if __name__ == "__main__":
    pos_word = Word_Make(positive_sentence)
    neg_word = Word_Make(negetive_sentence)

    pos_word_prob = Word_Probability(pos_word)
    pos_score = Classification(test_sentence, pos_word_prob)
    print(pos_word_prob)
    print("NB POS SCORE : " + str(pos_score))
    print("\n" * 2)


    neg_word_prob = Word_Probability(neg_word)
    neg_score = Classification(test_sentence, neg_word_prob)
    print(neg_word_prob)
    print("NB NEG SCORE : " + str(neg_score))

