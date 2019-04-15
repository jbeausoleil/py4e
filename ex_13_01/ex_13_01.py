from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get content of URL as string
url = input('Enter URL: ')
#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = 'http://py4e-data.dr-chuck.net/comments_183156.xml'
data = urlopen(url, context = ctx).read()

# Transform string into XML Tree
tree = ET.fromstring(data)

# Find all count elements
counts = tree.findall('comments/comment/count')

# Extract value of each element and sum total
sum = 0
for count in counts:
    sum += int(count.text)
print('Total:', sum)
