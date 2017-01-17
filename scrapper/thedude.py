import urllib2
from bs4 import BeautifulSoup
import requests
import unicodedata

url = "http://tabandchord.com/category/chord/chord-hindi/?first_letter=A"

hdr = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=hdr)), "lxml")

nav_data = soup.find_all("div", {"class": "navigation"})

# get page Url
pageList = []
for div in nav_data:
    page_url = div.findAll('a')
    for a in page_url:
        if 'http://' in a['href']:
            pageList.append(a['href'])

# get songs url
songList = []
for item in pageList:
    sou = BeautifulSoup(urllib2.urlopen(urllib2.Request(item, headers=hdr)), "lxml")
    g_data = sou.find("div", {"id": "a-z"})
    song_url = g_data.find_all("div", {"class": "title-cell"})
    for d in song_url:
        if d not in songList:
            songList.append(d.find('a').get('href'))
            print 'adding...' + d.find('a').get('href')

# parsing required data
server_url = 'http://127.0.0.1:8000/api/songs/'
for song in songList:
    soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(song, headers=hdr)), "lxml")
    title = soup.find("h1", {"class": "entry-title"}).getText().strip()
    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore')
    content = soup.find("div", {"class": "entry-content"})
    tabs_n_chord = ""
    for tag in content.findAll('p'):
        tabs_n_chord += str(tag)

    data = {
        "name": title,
        "tabs_and_chords": tabs_n_chord,
        "tags": "Hindi, Bollywood",
        "genre": 8
    }
    try:
        print data
        if tabs_n_chord != '':
            r = requests.post(server_url, data)
            print (r.status_code, r.reason)
    except:
        'Something is wrong!'
