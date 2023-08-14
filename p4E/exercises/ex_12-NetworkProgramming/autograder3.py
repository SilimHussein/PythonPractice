import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#this part of code is to ignore SSL certificate errors-
#it is used to disable hostname verification and Certificate verification
#it is vulnerable to man-in-the-middle attacks and should be done cautiously
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url -')
count = input('Enter Count:')
position = input('Enter position:')
print('Retrieving:', url)

for i in range(0,int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #Retrieve all of the anchor tags
    tags = soup('a', limit=int(position))
    for tag in tags:
        url = tag.get('href', None)
        print('Retrieving:',tag.get('href',None))