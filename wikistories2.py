
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

def randonum(b, e):
    return int(math.floor(random.uniform(b,e)))

page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
tablee = page_soup.find("table", {'class':'sortable'})
links= tablee.findAll("a")

for link in links:
    if "/wiki/" in link['href']:
        my_url = wiks + link['href']
        page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
        yo= page_soup.findAll("p")
        for i in range(6,8):
            sens=str(yo[i]).split(',')
            text=[]
            for sen in sens:
                try:
                    print(sen)
                    text.append(sen)
                except:
                    print('fail1')
        texts = texts + text[randonum(0,len(text)-1)]
            # num=randonum(6,10)
            # print(yo[num])
            # sens=str(yo[num]).split('.')
            # num=randonum(0,3)
            # text.append(sens[num])
    else:
        print('fail2')
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
