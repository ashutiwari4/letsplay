import requests
import json

server_url = 'http://127.0.0.1:8000/api/songs/'


def songinfo(query, songName):
    title = "cool"
    content = "hi"
    tabs_n_chord = "hello"

    data = {
        "name": title,
        "tabs_and_chords": tabs_n_chord,
        "tags": "Hindi, Bollywood",
        "genre": 15
    }
    try:
        print data
        if tabs_n_chord != '':
            r = requests.post(server_url, data)
            print json.loads(r._content)['id']
            print (r.status_code, r.reason)
    except:
        'Something is wrong!'

songinfo("as","as")