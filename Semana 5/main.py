import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = input('Enter - ')
data = urlopen(url).read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')

print("Counts: "+str(len(counts)))
sum=0

for i in counts:
    sum += int(i.text)

print("Sum: "+str(sum))
