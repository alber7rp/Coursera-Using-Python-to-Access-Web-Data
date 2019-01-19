from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

print("Retrieving: "+url)

for i in range(0, count):
    tags = soup.find_all('a')
    print("Retrieving: "+tags[position-1]['href'])
    html = urlopen(tags[position-1]['href']).read()
    soup = BeautifulSoup(html, "html.parser")
