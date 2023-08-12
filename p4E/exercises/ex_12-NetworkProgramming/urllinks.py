#using beautiful soup to parse through a website
#I have already installed beautiful soup, am not sure if i need to import from bs4
#directory.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#this part of code is to ignore SSL certificate errors- read about it.
#it is used to disable hostname verification and Certificate verification
#it is vulnerable to man-in-the-middle attacks and should be done cautiously
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))