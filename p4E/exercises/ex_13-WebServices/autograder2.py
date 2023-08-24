import urllib.request, urllib.parse, urllib.error
import ssl
import json 

#ignoring Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#user request for URL
url = input('Enter location:')

#default URL testing
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1737623.json"

#print retrieving message
print('Retrieving', url)

#open url, ignoring cert errors
uh = urllib.request.urlopen(url, context=ctx)

#reading the data 
data = uh.read()

#printing to match format text
print('Retrieved', len(data), 'characters')

#error checking, loading js
try:
    info = json.loads(data)
except:
    info = None

#calculating and printing count and sum
count = 0
tot = 0
for item in info['comments']:
    count = count + 1
    tot = int(item['count']) + tot

print('Count', count)
print('Sum', tot)




