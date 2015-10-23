__author__ = 'amerser1'
from bs4 import BeautifulSoup
import urllib2

top_cities_wiki_url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

url = top_cities_wiki_url
header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia


def scrape_top_cities(num=20):
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)

    table = soup.find("table", {"class": "wikitable sortable"})

    cities=list()
    ret=list()

    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if (len(cells) > 0):
            cities.append(cells[1].find(text=True)+ ", " + cells[2].find(text=True))

    for i in range(0,num,1):
        ret.append(cities[1])

    return ret