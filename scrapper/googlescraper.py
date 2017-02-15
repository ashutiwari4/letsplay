########### Python 2.7 #############
import httplib, urllib, base64

from play.models import Song,Genre

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '53e21303c12044b184a19871f97f5bf4',
}

params = urllib.urlencode({
    # Request parameters
    'q': Song.objects.all(),
    'count': '2',
    'offset': '0',
    'mkt': 'en-us',
    'safeSearch': 'Moderate',
})

try:
    conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)

    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
