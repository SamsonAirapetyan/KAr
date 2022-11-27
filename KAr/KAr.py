from bs4 import BeautifulSoup
import re

with open ("HL.html", 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

for links in soup.find_all('a', attrs= {'href' : re.compile('^https://')}):
     print(links.get('href'))



