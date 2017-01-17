import urllib2, sys
from bs4 import BeautifulSoup
import requests
import unicodedata

url = "http://tabandchord.com/2013/01/aa-bhi-jaa-mere-mehermaan-guitar-chords-atif-aslam/"

hdr = {'User-Agent': 'Mozilla/5.0'}
server_url = 'http://127.0.0.1:8000/api/songs/'
soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=hdr)), "lxml")
title = soup.find("h1", {"class": "entry-title"}).getText().strip()
title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore')
content = soup.find("div", {"class": "entry-content"})
tabs_n_chord = ""
for tag in content.findAll('p'):
    print tag
    print "============================================================"
    tabs_n_chord += str(tag)
print "########################################################="
print tabs_n_chord

data = {
    "name": title,
    "tabs_and_chords": tabs_n_chord,
    "tags": "Hindi, Bollywood",
    "genre": 8
}
headers = {"Content-type": "application/json"}
print data
r = requests.post(server_url, data)
print (r.status_code, r.reason)
print title
