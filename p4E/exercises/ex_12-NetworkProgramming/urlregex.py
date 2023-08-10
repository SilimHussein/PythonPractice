#search for link values with url input using regular expressions
import urllib.request, urllib.parse, urllib.error
import re
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
#openning url using uri library
html = urllib.request.urlopen(url, context=ctx).read()
#using regular expressions to find links in the above url
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
