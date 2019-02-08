from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = [
    '오늘은 즐거운 하루입니다',
    '오늘은 비가 올 것 같은데 내일은 비가 안 왔으면 좋겠네요.',
    '내일도 비가 올 것 같아요',
]


vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray())   # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(vector.vocabulary_)   # 각 단어의 인덱스가 어떻게 부여되었는지를 보여준다.
print("\n")


tfidfv = TfidfVectorizer().fit(corpus)
print(tfidfv.transform(corpus).toarray())
print(tfidfv.vocabulary_)
print("\n")

tfidfv2 = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}').fit(corpus)
print(tfidfv2.transform(corpus).toarray())
print(tfidfv2.vocabulary_)
print("\n")


tfidfv3 = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', ngram_range=(2, 3)).fit(corpus)
print(tfidfv3.transform(corpus).toarray())
print(tfidfv3.vocabulary_)
print("\n")


tfidfv4 = TfidfVectorizer(analyzer='char', token_pattern=r'\w{1,}', ngram_range=(2, 3)).fit(corpus)
print(tfidfv4.transform(corpus).toarray())
print(tfidfv4.vocabulary_)