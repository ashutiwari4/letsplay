import urllib,re,json

f = open('../img/00000001.jpg', 'wb')
url = urllib.unquote('http:\/\/www.bing.com\/cr?IG=DD6C6723DAD140FDB47C0F84DD3A58BB&CID=2C4EEE75ECA063E7379BE45FEDB2620C&rd=1&h=nr-rkMaw6H31agIINcdqaQbEkao3lo7upmbYp9HVyAw&v=1&r=http%3a%2f%2f2.bp.blogspot.com%2f-ypV-igMHG7I%2fUwsYzpXsHhI%2fAAAAAAAABlU%2fhDLUue8kcbs%2fs1600%2fAadat.jpg&p=DevEx,5014.1').decode('utf8')
s = re.findall(r'(https?://\S+)', url)[0]
f.write(urllib.urlopen(s).read())
f.close()

