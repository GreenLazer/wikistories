import nltk
import nltk.data
from nltk import pos_tag, word_tokenize
import random
import math
sents = ""

def randonum(b, e):
    return int(math.floor(random.uniform(b,e)))

def NextNNP(word, add):
    sent = ""
    word += 1
    while parts[word][1] !=  'NNP' and word + 1 < len(words):
        if add == True:
            sent += words[word] + " "
        word += 1
    return sent

with open('text.txt', 'r') as f:
    textuncoded = f.read()
    f.close()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
text = repr(textuncoded.decode('unicode-escape'))
sentances = sent_detector.tokenize(text)

for loop in sentances:
    words = nltk.word_tokenize(sentances[randonum(0,len(sentances))])
    parts = pos_tag(words)
    word = 0
    if parts[word][1] == 'NNP':
        sents += words[word] + " "
        sents += NextNNP(word, True)
    # elif parts[word][1] == 'PRP':
    #     sents += words[word] + " " + "PRP"
    #     sents += NextNNP(word, True)
    else:
        NextNNP(word, False)
        sents += words[word] + " "
        sents += NextNNP(word, True)

with open('scrambledtext.txt', 'w') as f:
    for i in sents:
        f.write(str(i))
