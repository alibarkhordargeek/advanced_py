from bs4 import BeautifulSoup
import re
import requests

r = requests.get('https://divar.ir/s/tehran')
soup = BeautifulSoup(r.text, 'html.parser')
agahi = soup.find_all('div', attrs = {'class':'kt-post-card__body'})

gheymat = list()
nam = list()
tavafoghi = list()

for gh in agahi:
    gh = re.findall(r'\d*۰,۰۰۰', gh.text)
    gheymat.append(gh)

for nm in agahi: 
    nm = re.findall(r'^.{20}', nm.text) 
    nam.append(nm)

for i in range(0, len(gheymat)):
    if gheymat[i] == []:
        tavafoghi.append(nam[i][0])

for nm in tavafoghi:
    print(nm)