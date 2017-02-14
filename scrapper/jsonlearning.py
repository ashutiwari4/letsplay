import json

f = open("./jsondata.json")
data = json.load(f)
# print json.dumps(data)
for item in data['value']:
    link = item['hostPageDisplayUrl']
    thumbnail = item['thumbnailUrl']
    contentURl = item['contentUrl']
    encodingFormat = item['encodingFormat']
    print thumbnail

#print json.dumps(node)
