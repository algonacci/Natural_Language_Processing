from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

sentence = 'Indonesia bisa menjadi negara yang terbaik dengan karya anak bangsa.'

output = stemmer.stem(sentence)
print(output)