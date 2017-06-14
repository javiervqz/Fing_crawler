import urllib
from lxml.html import parse
import bs4 as bs
import sys



url_dir= 'http://fing.uach.mx/facultad/2015/09/24/directorio_docente/'
url_main = 'http://fing.uach.mx'
parsed = parse(url_dir)
doc = parsed.getroot()
links = doc.findall('.//div[@id="listalinks"]/p/a')

i = 1.0
for link in links:
	prof_name = link.text_content()
	file = open(prof_name+".txt", "w")
	profurl = url_main+link.get("href")
	html = urllib.urlopen(profurl).read()
	soup_prof = bs.BeautifulSoup(html, 'lxml')

	for info in soup_prof.findAll("div", attrs ={'id' : None, 'align': None, 'class': None}):
		if info is not None:
			#file.write(info.text.encode('utf-8') + '\n')
			file.write(str(info) + ' \n' + prof_name.encode('utf-8') )
	a = (i/len(links))*100
	print 'Writing file ' "%.2f" % a, '%'
	sys.stdout.write("\033[F") # Cursor up one line
	i += 1
	file.close()
print '\n Done!'
