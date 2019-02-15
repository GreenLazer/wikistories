import nltk

with open('text.txt', 'r') as f:
    textuncoded = f.read()
    f.close()

text = repr(textuncoded.decode('unicode-escape'))
tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
print tagged
