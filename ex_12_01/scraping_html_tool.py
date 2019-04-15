from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Establish connection with URL
url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
#url = 'http://py4e-data.dr-chuck.net/comments_183154.html'
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the <SPAN> tags
sum = 0
spans = soup('span')
for tag in spans :
    numbers = re.findall('[0-9]+', tag.decode())
    # Cumulative sum of numbers in numbers
    for i in numbers :
        i = int(i)
        sum = sum + i
    print('Number: ',sum)
