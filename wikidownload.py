import requests
from bs4 import BeautifulSoup
my_url='https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
wiks='https://en.wikipedia.org'
hrefs = []
paras = []
hrefnum = 0

page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
links = page_soup.findAll("a")

for link in links:
    if link.parent.name == 'i':
        if link.parent.parent.name == "td" or link.parent.parent.name == "th":
            page_name = link.get('href')
            if not any(x in page_name for x in ("franchise","series","trilogy","films","filmography","Anthology", "Extended_Universe", "Marvel_Studios")):
                hrefs.append(page_name)

for href in hrefs:
    print(hrefnum)
    hrefnum += 1
    my_url = wiks + href
    page_soup = BeautifulSoup(requests.get(my_url).text, "html.parser")
    plotstart = page_soup.findAll('h2')[1]
    plotend = page_soup.findAll('h2')[2]
    current = plotstart.next_sibling
    while current != plotend:
        if current.name == 'p':
            paras.append(current)
        current = current.next_sibling
with open('alltext.html', 'w') as f:
    for i in paras:
        f.write(str(i))
#313,464 words 
