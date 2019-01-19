from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input('Enter - ')

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all('tr', {'id': re.compile(r'nonplayingnow.*')})

for i in tags:
    casa = i.find("td", {'class': re.compile(r'team-home')}).find("a")
    visitante = i.find("td", {'class': re.compile(r'team-away')}).find("a")
    print ("Partido-> "+casa.get_text()+" vs "+visitante.get_text())
