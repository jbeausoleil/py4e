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
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#url = 'http://py4e-data.dr-chuck.net/known_by_Dewi.html'
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))

# Retrieve all of the <anchor> tags
for i in range(count) :
    html = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    number = 0
    for anchor in anchors :
        number += 1
        if number == position :
            url = anchor.get('href', None)
            if i == count - 1 :
                print(anchor.contents[0])
            break
