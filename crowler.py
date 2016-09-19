import urllib2
from bs4 import BeautifulSoup

url = 'http://www.polityka.pl/forum/'

page = urllib2.urlopen(url)
content = page.read()
soup = BeautifulSoup(content)

print soup.find_all('li')
