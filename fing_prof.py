import urllib, re
import HTMLParser
from BeautifulSoup import *


url_dir= 'http://fing.uach.mx/facultad/2015/09/24/directorio_docente/'
url_main = 'http://fing.uach.mx'
html = urllib.urlopen(url_dir).read()
urlText = []

class parseText(HTMLParser.HTMLParser):
	def handle_data(self, data):
		if data != '\n':
			urlText.append(data)

lParser = parseText()
lParser.feed(html)
lParser.close()




# soup_dir = BeautifulSoup(html)
# tags = soup_dir('a')
#
#
# most_prof = []
# for tag in tags:
# 	url = tag.get('href')
# 	try:
# 		num = re.findall('[0-9]{4}', url)
# 		if url.startswith('/facultad') and int(num[0]) > 2014:
# 			most_prof.append(url)
# 	except:
# 		continue
#
# file = open("divtest.txt", "w")
# for prof in most_prof:
# 	url_prof = url_main + str(prof)
# 	html_prof = urllib.urlopen(url_prof).read()
# 	soup_prof = BeautifulSoup(html_prof)
# 	tags1 = soup_prof("li")
# 	tags2 = soup_prof("div")
# 	tags3 = soup_prof("a")
# 	list_prof = []
# 	list_mat = []
# 	for tag in tags2:
# 		finder = re.compile(r'\bInteligencia\b| \balgoritmos\b | \bcomputadora\b', flags = re.I | re.X)
# 		subjects = finder.findall(str(tag))
# 		if subjects:
# 			file.write(str(prof) + '\n' + str(tag) + '\n'+'\n')
#
# file.close()


# tags = suop_prof('li')
# for tag in tags:
# 	print tag

#i = 0
#pcount = raw_input('Enter count: ')
#position = raw_input('Enter position: ')
#count = int(pcount)
#while i < count:
#	names = list()
#	for tag in tags:
#		url1 = tag.get('href', None)
#		names.append(str(url1))
#	url = names[int(position)-1]
#	html = urllib.urlopen(url).read()
#	soup = BeautifulSoup(html)
#	tags = soup('a')
#	i += 1
#	print  names[int(position)-1]
