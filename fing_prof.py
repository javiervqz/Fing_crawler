import urllib
from lxml.html import parse
import bs4 as bs



url_dir= 'http://fing.uach.mx/facultad/2015/09/24/directorio_docente/'
url_main = 'http://fing.uach.mx'
parsed = parse(url_dir)
doc = parsed.getroot()
links = doc.findall('.//div[@id="listalinks"]/p/a')
file = open("divtest.txt", "w")
for link in links:
	prof_name = link.text_content()
	profurl = url_main+link.get("href")
	html = urllib.urlopen(profurl).read()
	soup_prof = bs.BeautifulSoup(html, 'lxml')

	for info in soup_prof.findAll("div", attrs ={'class' : None}):
		print info.div
file.close()


# 	parsed = parse(profurl)
# 	doc = parsed.getroot()


	# raw = doc.findall('.//div/h4')
	# finder = re.compile(r'\bCursos\b | \bImpartidos\b', flags = re.I | re.X)
	# for tag in raw:
	# 	aver = finder.findall(tag.text_content())
	# 	if aver:
	# 		print prof_name, tag
