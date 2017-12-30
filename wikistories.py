import random
import math
import nltk
import csv
from nltk import tokenize
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
text = []
texts = []
wiks='https://en.wikipedia.org'

def randonum(b, e):
    return math.floor(random.uniform(b,e))

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
tablee = page_soup.find("table", {'class':'wikitable'})
links=tablee.findAll("a")

for link in links:
    if "/wiki/" in link['href']:
        my_url = wiks + link['href']
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        yo= page_soup.findAll("p")
        for i in range(6,9):
            sens=str(yo[i]).split(',')
            text=[]
            for sen in sens:
                try:
                    print(sen)
                    text.append(sen)
                except:
                    print('fail1')
        texts.append(text)
    else:
        print('fail2')

print(len(texts))

print("fetching end")
final=''
#
# rng=len(texts)
# for m in range(5):
#     for i in range(0,17):
#         print("sentance:" + str(i))
#         for k in range(rng):
#             artnum=randonum(0,rng)
#             try:
#                 final= final + texts[artnum][i]
#                 break
#             except:
#                 print("artnum:" + str(artnum)) #exept autmatical ends loop? is there a go to?
# print(final)
