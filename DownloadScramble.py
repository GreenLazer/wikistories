import nltk
from nltk import pos_tag, word_tokenize
sents = ""

with open('text.txt', 'r') as f:
    textuncoded = f.read()
    f.close()

text = repr(textuncoded.decode('unicode-escape'))
words = nltk.word_tokenize(text)
PoS = pos_tag(words)

word = 0
while word < len(words):
    wordT = PoS[word] #assign wordT part of speech connected to current word
    if wordT[1] == 'NNP': #if part of speech is proper noun add word to sents, moce to next word, and start scanning
        sents += words[word] + " "
        word += 1
        wordT = PoS[word]
        while wordT[1] != 'NNP' and word < len(words): #loops through words until find next proper noun or finishes all words
            print words[word]
            wordT = PoS[word]
            word+= 1
    else:
        sents += words[word] + " "
        word += 1

with open('scrambledtext.txt', 'w') as f:
    for i in sents:
        f.write(str(i))
