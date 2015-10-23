__author__ = 'amerser1'
from Scrapers import scrape_capitals, scrape_top_cities

capitals=list()
topcities=list()
mycities=['Calgary, Alberta', 'Montreal, Quebec', 'Victoria, British Columbia']

topcities= scrape_top_cities.scrape_top_cities(num=15)
capitals= scrape_capitals.scrape_capitals()
print len(topcities)
print len(capitals)
print list(set(capitals) | set(mycities) | set(topcities))
print len(list(set(capitals) | set(mycities) | set(topcities)))