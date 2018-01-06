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
linknum = 1

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
    print(linknum)
    linknum += 1
    my_url = wiks + link
    page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
    try:
        plot = page_soup.findAll('h2')[1]
        endplot = page_soup.findAll('h2')[2]
        current = plot.next_sibling
        while current != endplot:
            paras.append(current)
            current = current.next_sibling

        for para in paras:
            sens=str(para).split(',')
            text=[]
            text.append(sens[randonum(0,len(sens)-1)])
            print("new para")
        texts = texts + text[randonum(0,len(text)-1)]
    except:
        print('fail')
            # num=randonum(6,10)
            # print(yo[num])
            # sens=str(yo[num]).split('.')
            # num=randonum(0,3)
            # text.append(sens[num])
        # link= links[math.floor(random.uniform(0,10))]
        # print(link['href'])
        # new_link=wiks + link['href']
        #
        # while new_link != wiks + link['href']:
        #     link= links[math.floor(random.uniform(0,10))]
        #     new_link=wiks + link['href']
        #
        # links.append(new_link)
        # print(new_link)
        # my_url=new_link


print(texts)
