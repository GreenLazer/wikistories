import json
import urllib2
import re

chck =False

things = ''
url = 'https://en.wikipedia.org/w/api.php?action=query&titles=List_of_Academy_Award-winning_films&prop=revisions&rvprop=content&format=json'

data= urllib2.urlopen(url)
jsondata =json.load(data)

please = str(jsondata['query']['pages'])
print please
# links = re.findall("\\'\\'\[\[", please)

for i in range(len(please)):
    if please[i]=='\'' and please[i+1]== '[':
        chck =True
    if chck==True:
        things = things + please[i]
    if please[i]==']':
        chck=False
# print links
print things
