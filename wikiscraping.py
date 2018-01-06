
import random
import math
import requests
from bs4 import BeautifulSoup
my_url='https://en.wikipedia.org/wiki/Portal:Contents/Culture_and_the_arts'



links=[my_url]
wiks='https://en.wikipedia.org'

i = 0

while i<9:
    soup = BeautifulSoup(requests.get(my_url).text, "html.parser")

    links = soup.find_all('a')
    link= links[int(math.floor(random.uniform(0,10)))]
    print(link.get('href'))
    new_link=wiks + link['href']

    while new_link != wiks + link.get('href'):
        link= links[int(math.floor(random.uniform(0,10)))]
        new_link=wiks + link['href']

    links.append(new_link)
    print(new_link)
    my_url=new_link
    i+=1
