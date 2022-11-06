import requests
from nltk import sent_tokenize

paragraph = requests.get('https://github.com/rasyidev/well-known-datasets/raw/main/rendang.txt').text
paragraph = sent_tokenize(paragraph)

max_chunk = 50
current_chunk = 0
chunks = []

for sentence in paragraph:
    if len(chunks) == current_chunk + 1:
        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
            chunks[current_chunk].extend(sentence.split(' '))
        else:
            current_chunk += 1
            chunks.append(sentence.split(' '))
    else:
        chunks.append(sentence.split(' '))

for chunk_id in range(len(chunks)):
    chunks[chunk_id] = ' '.join(chunks[chunk_id])

print(chunks[0])
print(len(chunks))