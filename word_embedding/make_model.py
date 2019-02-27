import json
import gensim

'''
- 목적 : Token으로 저장된 파일을 불러와 gensim의 word2vec에 입력한다.
'''

with open('corpus_token.txt', 'r', encoding="utf-8") as f:
    text = f.readlines()
    data = json.loads(text[0])

print(data)


embedding = gensim.models.Word2Vec(data, size=100, window=7, negative=3, min_count=5)
print(embedding)


embedding.save('my.model')      # weight vector 모델을 저장한다.



model = gensim.models.Word2Vec.load('my.model')         # model을 불러와서 하고 싶은 작업을 해준다.
print(model.wv['서울'])
print(model.most_similar('서울'))


word = "서울"  # for any word in model
i = model.max_final_vocab
print(i)
# model.index2word[i] == word  # will be true