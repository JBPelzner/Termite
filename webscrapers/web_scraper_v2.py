## Source: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

"""Note: this version is the most ready to be used, with the links returned being relative links
which can be concatenated to the input URL to navigate to the corresponding page
"""

# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://www.' + input('Enter the URL for the website: ')
print(url)

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# create a blank list where all the links will be compiled
links = []

# To download the whole data set, let's do a for loop through all a tags
line_count = 1 #variable to track what line you are on
for one_a_tag in soup.findAll('a'):  #'a' tags are for links

    # if line_count >= 36: ##code for text files starts at line 36

    link = one_a_tag['href']

    links.append(link)
    # download_url = 'http://web.mta.info/developers/'+ link
    # urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 

    time.sleep(0.1) #pause the code for a sec

    #add 1 for next line
    line_count +=1

print(links)