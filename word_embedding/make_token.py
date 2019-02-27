from konlpy.tag import Komoran
import json

'''
- 목적 : corpus.txt라는 문장이 담겨있는 파일을 Token으로 변환시켜 corpus_token.txt라는 파일을 만든다.

영어에서는 NLTK를 활용하여 문장을 Token으로 나누어준다.
한국어에서는 형태소 분석기를 사용해 문장을 형태소 단위로 나누어 준다.
여기서는 Konlpy 라이브러리의 Komoran 모듈을 사용해 문장을 Token으로 변환시켜주었다.
'''

def make_token(input_file, output_file):
    komoran = Komoran()
    token_txt_file = open(output_file, "w", encoding="utf-8")
    list = []

    with open(input_file, 'r', encoding="utf-8") as f:
        text = f.readlines()
        num = 0

        for i in range(0, len(text)):
            sentence = text[i].strip()

            morphs = komoran.morphs(sentence)
            print(morphs)
            list.append(morphs)

        print(num)

        my_json_string = json.dumps(list, ensure_ascii=False)
        token_txt_file.write(my_json_string)


if __name__ == "__main__":
    make_token("corpus.txt", "corpus_token.txt")