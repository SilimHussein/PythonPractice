from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate Error- again, be careful with this one- man-in-the-middle attacks
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url-')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retriever all the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)