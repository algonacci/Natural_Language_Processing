import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import warnings
warnings.filterwarnings("ignore")

model = load_model("model.h5")

print("==========================================================")
print("==========================================================")
print("==========================================================")
print("==========================================================")
print("==========================================================")
seed_text = str(input("Enter a seed text: "))
print("==========================================================")
print("==========================================================")
print("==========================================================")
next_words = int(input("Enter the number of words you want to generate: "))
print("==========================================================")
print("==========================================================")
print("==========================================================")
print("==========================================================")
print("==========================================================")

tokenizer = Tokenizer()

data = open('linkedin.txt').read()
corpus = data.lower().split("\n")

tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])

special_words = ["object", "profession", "subject", "institution", "person"]

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding="pre")
    predicted = model.predict(token_list, verbose=0)
    predicted = np.argmax(predicted[0], axis=-1)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word
    # uppercasing any word in seed_text if the word is in special words
    for word in special_words:
        if word in seed_text:
            seed_text = seed_text.replace(word, word.upper())

print(seed_text)