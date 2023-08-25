import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ignore SSL certificate errors.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#prompt for user location, test without parameters to handle "No address"
address = input('Enter location: ')
if len(address) < 1:
    print('No address')
    quit()

# setting up api
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
parms = dict()
parms['address'] = address
parms['key'] = 42

#using urllib.parse.urlencode() to properly url encode the address parameter
url = serviceurl + urllib.parse.urlencode(parms)

#retrieving the url, opening it, and decoding it from byte to string
print('Retrieving', url)
uh = urllib.request.urlopen(url, context = ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure to Retrieve ====')
    print(data)

print(json.dumps(js, indent =4))

