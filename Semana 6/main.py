import json
from urllib.request import urlopen

url = input('Enter - ')
data = urlopen(url).read()
info = json.loads(data)

print("Counts: "+str(len(info['comments'])))
sum=0

for i in info['comments']:
    sum += int(i['count'])

print("Sum: "+str(sum))
