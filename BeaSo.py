from BeautifulSoup import *
import urllib
import re

host = 'http://python-data.dr-chuck.net/comments_'

url = raw_input('Enter - ')
html = urllib.urlopen(host+url+'.html').read()

soup = BeautifulSoup(html)

tags = soup('span')
su = 0
for tag in tags:
	num = tag.contents[0]
	n = int(num)
	su += n
print su
