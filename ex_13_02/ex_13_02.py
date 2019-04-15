import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create service URL
serviceurl = ''

address = input('Enter URL: ')
#address = 'http://py4e-data.dr-chuck.net/comments_42.json'
#address = 'http://py4e-data.dr-chuck.net/comments_183157.json'
#if len(address) < 1 : break

#Redefine Address to URL
url = serviceurl + address

#Bring down data from URL
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

#Define JS as json
info = json.loads(data)

sum = 0

for item in info['comments']:
    sum = int(item['count']) + sum
print(sum)
