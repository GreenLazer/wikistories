import random
import math
import nltk
import csv
from nltk import tokenize
import requests
from bs4 import BeautifulSoup
my_url='https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
text = []
texts = ''
wiks='https://en.wikipedia.org'
fail = True
links = []
paras = []
linknum = 23

def randonum(b, e):
    return int(math.floor(random.uniform(b,e)))

page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
tablee = page_soup.findAll("i")

for row in tablee:
    try:
        links.append(row.find('a')['href'])
    except:
        fail = True
for link in links[linknum:290]:
    print(linknum)
    linknum += 1
    my_url = wiks + link
    page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
    try:
        plot = page_soup.findAll('h2')[1]
        endplot = page_soup.findAll('h2')[2]
        current = plot.next_sibling
        while current != endplot:
            if current.name == 'p':
                print current.name
                paras.append(current)
            current = current.next_sibling
    except:
        print('fail')
with open('alltext.html', 'w') as f:
    for i in paras:
        f.write(str(i))
