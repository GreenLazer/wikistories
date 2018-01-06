import random
import math
import nltk
import csv
from nltk import tokenize
import requests
from bs4 import BeautifulSoup
my_url='https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
text = []
texts = []
wiks='https://en.wikipedia.org'
fail = True
links = []
paras = []

def randonum(b, e):
    return int(math.floor(random.uniform(b,e)))

page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
tablee = page_soup.findAll("i")

for row in tablee:
    try:
        links.append(row.find('a')['href'])
    except:
        fail = True

for link in links[20:494]:
    my_url = wiks + link
    page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")

    plot = page_soup.findAll('h2')[1]
    endplot = page_soup.findAll('h2')[2]
    current = plot.next_sibling
    while current != endplot:
        paras.append(current)
        current = current.next_sibling

    for para in paras:
        sens=str(para).split(',')
        text=[]
        for sen in sens:
            try:
                print(sen)
                text.append(sen)
            except:
                print('fail1')
    texts.append(text)

print(len(texts))

print("fetching end")
final=''

rng=len(texts)
for m in range(5):
    for i in range(0,17):
        print("sentance:" + str(i))
        for k in range(rng):
            artnum=randonum(0,rng)
            try:
                final= final + texts[artnum][i]
                break
            except:
                print("artnum:" + str(artnum)) #exept autmatical ends loop? is there a go to?

print(final)
