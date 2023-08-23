import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
#ignoring Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#user request for URL
url = input('Enter url:')

#default URL testing
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1737622.xml"

#print retrieving message
print('Retrieving', url)

#open url, ignoring cert errors
uh = urllib.request.urlopen(url, context=ctx)

#reading the data 
data = uh.read()

#counting total number of characters read
print('Retrieved', len(data), 'characters')

#converting xml form string to tree represantation
tree = ET.fromstring(data)

#searching for count using Xpath selecoter string
counts = tree.findall('.//count')

#formatted output to match sample execution
print('Count', len(counts))
print('Sum', sum([int(item.text) for item in counts]))