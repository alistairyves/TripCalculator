__author__ = 'amerser1'
import requests
import Resources
import os

google_api_key = "AIzaSyAsrkhipASffKcs4kttlfoUmMEBa6EHPqA"
base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
output = "json"

filepath = os.path.dirname(Resources.__file__) + '\\' + "cities.txt"
f = open(filepath, 'r+')
cities = f.read().rstrip().split(("\n"))
f.close()

startingCity = "Montreal"
endingCity = "Calgary"
cities.remove("Calgary, Alberta")
cities.remove("Montreal, Quebec")

payload = {'origins': 'Calgary, Alberta', 'destinations': 'Montreal, Quebec', 'key': google_api_key}
r = requests.get(base_url, params=payload)
print r.text
