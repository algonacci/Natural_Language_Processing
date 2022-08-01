from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('better', pos='a'))
print(lemmatizer.lemmatize('best', pos='a'))
print(lemmatizer.lemmatize('worse', pos='a'))
print(lemmatizer.lemmatize('run'))