import os
import Resources

#this is a script which will build my list of cities to visit
#run if you want to repopulate the list
__author__ = 'amerser1'
from Scrapers import scrape_capitals, scrape_top_cities

capitals=list()
topcities=list()
mycities=['Calgary, Alberta', 'Montreal, Quebec', 'Victoria, British Columbia']

topcities= scrape_top_cities.scrape_top_cities(num=15)
capitals= scrape_capitals.scrape_capitals()

cities=list(set(capitals) | set(mycities) | set(topcities))
filepath=os.path.dirname(Resources.__file__)+'\\'+"cities.txt"

if os.path.exists(filepath):
    exit()
f = open(filepath, 'w')
for str in cities:
    f.write(str + "\n")
    print str
f.close()