from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter your start url:')
co = input('Enter your count:')
posi = input('Enter your position:')





for i in range(int(co)):
	html = urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	number = 0
	for tag in tags:
		number += 1
		if number == int(posi):
			url = tag.get('href')
			if i == int(co)-1:
				print(tag.contents[0])
			break
