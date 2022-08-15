import pandas as pd
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer
import requests

paragraph = requests.get('https://github.com/rasyidev/well-known-datasets/raw/main/rendang.txt').text

sentence = nltk.sent_tokenize(paragraph)

word_table = []
for i in range(len(sentence)):
    word = re.sub(r'[^\w]', ' ', sentence[i])
    word = word.lower()
    word = word.split()
    word = ' '.join(word)
    word_table.append(word)

cv = CountVectorizer()
X = cv.fit_transform(word_table)
print(X)