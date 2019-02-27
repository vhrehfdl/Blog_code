import re

'''
- 목적 : 한겨레 기사는 여러 문장으로 단락이 구성되어져 있다.그래서 문장 by 문장으로 잘라서 정리를 한 후 corpus.txt라는 파일을 만들어준다.
'''

def make_corpus(input_file, output_file):
    txt_file = open(output_file, "w", encoding="utf-8")

    with open(input_file, 'r', encoding="utf-8") as f:
        text = f.readlines()
        num = 0

        for i in range(0, len(text)):
            sentence_list = text[i].strip()
            sentence = sentence_list.split('.')

            for j in range(0, len(sentence)):
                if len(sentence[j].strip()) > 3:
                    last_sentence = sentence[j].strip()
                    print(last_sentence)
                    txt_file.write(last_sentence + "\n")

                    num += 1

        print(num)



if __name__ == "__main__":
    make_corpus("Han.txt", "corpus.txt")    # input_file에는