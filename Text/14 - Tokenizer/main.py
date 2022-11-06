from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'I love my dog',
    'I love my cat',
    'You love my dog!',
]

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

print(word_index)
# {'love': 1, 'my': 2, 'i': 3, 'dog': 4, 'cat': 5, 'you': 6}