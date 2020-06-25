## Source: https://www.youtube.com/watch?v=bIeN64tBxWM

"""Note: the functionality in the try/except statements has not been built out yet
"""

# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageURL):

  global pages
  # html = urlopen('http://www.' + input('Enter the URL for the website: '))
  html = urlopen('http://www.' + pageURL)

    
  print(html)

  # Parse HTML and save to BeautifulSoup object¶
  soup = BeautifulSoup(html, "lxml")

  # create a blank list where all the links will be compiled
  links = []

  try:
      print()

  except AttributeError:
      print("This page is missing something! No worries though!")

  for link in soup.findAll("a", href=re.compile("^https://")):
    if 'href' in link.attrs:
      if link.attrs['href'] not in pages:
        newPage = link.attrs['href']
        print('---------------------- \n', newPage)
        pages.add(newPage)
        getLinks(newPage)

getLinks("")