import urllib2
from bs4 import BeautifulSoup
import requests
import unicodedata
import json
import urllib, httplib
import re

#urlList = []
url = ("http://tabandchord.com/category/chord/chord-hindi/?first_letter=A")
#urlList.append("http://tabandchord.com/tab/tab-hindi/?first_letter=A")

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
server_details_url = "http://127.0.0.1:8000/api/song_details/"


class SongImageForm(object):
    def __init__(self, thumbnail, image_url, link, image_encoding, accent_color):
        self.thumbnail = thumbnail
        self.image_url = image_url
        self.link = link
        self.image_encoding = image_encoding
        self.accent_color = accent_color


headers = {
    # Request headers
    # 'Ocp-Apim-Subscription-Key': '53e21303c12044b184a19871f97f5',
    'Ocp-Apim-Subscription-Key': '53e21303c12044b184a19871f97f5bf4',
}


def songinfo(query, id):
    print 'Searching for ' + query
    query = re.sub("Chords", ",", query, flags=re.I)
    query = re.sub("Tabs", ",", query, flags=re.I)
    query = re.sub("Guitar Chords", ",", query, flags=re.I)
    params = urllib.urlencode({
        # Request parameters
        'q': query,
        'count': '2',
        'offset': '0',
        'mkt': 'en-us',
        'safeSearch': 'Moderate',
    })

    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        d = response.read()
        print d
        data = json.loads(d)
        print '2. Image data found!'
        # print(data)
        for item in data['value']:
            detailsData = {
                "name": id,
                "thumbnail": '/img/thumbnail/' + id + "." + item['encodingFormat'],
                "image_url": '../img/image/' + id + "." + item['encodingFormat'],
                "link": item['hostPageDisplayUrl'],
                "image_encoding": item['encodingFormat'],
                "accent_color": item['accentColor']
            }

            f = open('../img/image/' + id + "." + item['encodingFormat'], 'wb')
            oz = urllib.unquote(item['contentUrl']).decode('utf8')
            s = re.findall(r'(https?://\S+)', oz)[0]
            f.write(urllib.urlopen(s).read())
            f.close()

            f = open('../img/thumbnail/' + id + "." + item['encodingFormat'], 'wb')
            f.write(urllib.urlopen(item['thumbnailUrl']).read())
            f.close()
            print '3. thumbnail written: ' + id

            try:
                print detailsData
                if detailsData['image_url'] != '':
                    ashu = requests.post(server_details_url, detailsData)
                    print (ashu.status_code, ashu.reason)
                    print '4. song details posted! finally this song'
            except:
                print '4. Something is wrong gettimh details!'
        conn.close()
    except Exception as e:
        print '2. Something wrong in gettng image '
        print("2. [Errno {0}] {1}".format(e.errno, e.strerror))
    return


for song in songList:
    soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(song, headers=hdr)), "lxml")
    title = soup.find("h1", {"class": "entry-title"}).getText().strip()
    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore')
    content = soup.find("div", {"class": "entry-content"})
    chords = ""
    for tag in content.findAll('p'):
        chords += str(tag)




    data = {
        "name": title,
        "chords": chords,
        "tags": "Hindi, Bollywood",
        "genre": 2
    }
    try:
        if chords != '':
            r = requests.post(server_url, data)
            print '1.chords posted:  '
            print (r.status_code, r.reason)
            songinfo(title, str(json.loads(r._content)['id']))

    except:
        print '1. Something is wrong while getting tabs'
