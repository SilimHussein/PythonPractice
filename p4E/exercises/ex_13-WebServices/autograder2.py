import urllib.request, urllib.parse, urllib.error
import ssl, json

#ignoring Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#user request for URL
url = input('Enter url:')

#default URL testing
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

#print retrieving message
print('Retrieving', url)

#open url, ignoring cert errors
uh = urllib.request.urlopen(url, context=ctx)

#reading the data 
data = uh.read()

#printing to match format text
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count:', len(info))




