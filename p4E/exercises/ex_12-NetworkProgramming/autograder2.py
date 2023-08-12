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

numbers = []
for tag in soup.find_all(['p','span','div'], text=True):
    try:
        number = float(tag.text)
        numbers.append(number)
    except ValueError:
        pass
#count numbers and calculate the sum
num_count = len(numbers)
num_sum = sum(numbers)

print('count:', num_count)
print('sum:', int(num_sum))

