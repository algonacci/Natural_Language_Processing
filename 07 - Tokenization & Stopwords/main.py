from nltk import word_tokenize
from nltk.corpus import stopwords

sentences =  'Hello World! My name is Eric. I love Python.'
stopwords = set(stopwords.words('english'))

words = word_tokenize(sentences)

filtered = [w for w in words if not w in stopwords]

print(filtered)