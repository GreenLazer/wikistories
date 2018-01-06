
import random
import math
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://en.wikipedia.org/wiki/Portal:Contents/Culture_and_the_arts'



links=[my_url]
wiks='https://en.wikipedia.org'

i = 0

while i<9:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    article = page_soup.find("div", {'id':'mw-content-text'})
    links= article.findAll("a")

    link= links[math.floor(random.uniform(0,10))]
    print(link['href'])
    new_link=wiks + link['href']

    while new_link != wiks + link['href']:
        link= links[math.floor(random.uniform(0,10))]
        new_link=wiks + link['href']

    links.append(new_link)
    print(new_link)
    my_url=new_link
    i+=1
