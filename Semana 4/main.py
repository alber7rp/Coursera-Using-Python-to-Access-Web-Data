from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
spans = soup.find_all('span', {'class': re.compile(r'comments')})
for span in spans:
    sum += int(span.contents[0])

print("Count: " + str(len(spans)))
print("Sum: "+ str(sum))
