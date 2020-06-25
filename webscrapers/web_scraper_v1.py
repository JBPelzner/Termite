## Source: https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
### THE PACKAGES IN THIS LINK ARE OUTDATED

"""Note: this version is somewhat functional, although it does not return even the relative links
from the footer of the HTML page that are returned in the v2 scraper
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
# import urllib.request
import re

def getLinks(url):
    print(url, '\n ----------')

    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, features="lxml")
    # soup = BeautifulSoup(html_page, 'html.parser')

    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}): ##original code
    # for link in soup.findAll('a', attrs={'class': 'Fx4vi'}):
        links.append(link.get('href'))

    for link in links:
      print(link, '\n')

    

# print( getLinks("https://www.google.com" ) )
print( getLinks("https://www." + input("Enter website URL here: ")) )