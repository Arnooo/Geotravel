import json
import re
import mechanize
from unidecode import unidecode
from urllib2 import quote
br = mechanize.Browser()

def send_query(query):
    try:
        return br.open(query)
    except:
        #print "Error: Cannot execute query = "+query
        return 0

### MAIN
print "########### Geotravel ###########"

json_data=open('Vietnam_SelCities.geojson')
data = json.load(json_data)
json_data.close()
for city in data["features"]:
    cityName = unidecode(city["properties"]["name"])
    escaped_string = quote(cityName)
    success = send_query("http://wikitravel.org/en/"+escaped_string) 
    if success:
        print "City "+cityName + ":\t\thttp://wikitravel.org/en/"+escaped_string
    else:
        print "City "+cityName+":\t\tNot supported"

print "########### END ###########" 
