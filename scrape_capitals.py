__author__ = 'amerser1'
from bs4 import BeautifulSoup
import urllib2

capitals_wiki_url = "https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States"

url = capitals_wiki_url
header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
req = urllib2.Request(url, headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)

table = soup.find("table", {"class": "wikitable sortable"})

for row in table.findAll("tr"):
    cells = row.findAll("td")
    if (len(cells) > 0):
        print cells[3].find(text=True)+ ", " + cells[0].find(text=True)
